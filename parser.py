import yaml
import re
import uuid
import os
import json
import logging

logger = logging.getLogger(__name__)

tests = []


"""
Body Model = {"key": {"type": "datatype", "variable": ""}}
"""


def validate_path(endpoint, data):
    resp = {"errors": [], "path": endpoint}
    pattern = r"\{(.*?)\}"
    parameters = {}
    try:
        parameters = data["parameters"]
    except KeyError:
        pass
    path_params = re.findall(pattern, endpoint)
    if path_params:
        for pp in path_params:
            try:
                parameters[pp]
            except KeyError:
                resp["errors"].append(
                    "Parameter definition not found for {}".format(pp)
                )
                return resp
    ops = []
    methods = ["get", "put", "post", "delete"]
    ops = [i for i in methods if i in list(data.keys())]
    if len(ops) == 0:
        resp["errors"].append("No operations found")
    if ops:
        for item in ops:
            try:
                responses = data[item]["responses"]
            except KeyError:
                resp["errors"].append("{} no responses found!".format(item))
    return resp


def validate(data):
    d = yaml.load(data, yaml.Loader)
    errors = []
    servers = []
    paths = []
    validpaths = []
    try:
        paths = d["paths"]
    except KeyError:
        errors.append("No paths found!")
    if len(paths) == 0:
        errors.append("No paths found!")
    if errors:
        return errors
    for k, v in paths.items():
        validpaths.append(validate_path(k, v))
    return errors, validpaths


def generate_testid(testids):
    i = os.urandom(2).hex().upper()
    if i in testids:
        generate_testid(testids)
    return i


class Method(object):
    def __init__(self, parserobj, testid, method_data):
        self.parserobj = parserobj
        self.testid = testid
        self.method_data = method_data
        self.request_params = []
        self.assertions = []
        self.assertion_codes = {}
        self.assertion_code_list = []
        self.assertion_keys = []
        self.param_keys = []
        self.dynamic_variables = []
        self.body_params = []
        self.path_params = []
        self.query_params = []
        self.header_params = []
        self.is_body = False
        self.body_content_type = "application/json"

    def _generate_sample_data(self, dtype, tid):
        mapping = {
            "string": "{}TestData".format(tid),
            "array": str(["{}TestData".format(tid), "{}TestData".format(tid)]),
            "integer": 100,
            "boolean": "false",
        }
        return mapping[dtype]

    def _generate_key(self):
        k = os.urandom(3).hex()
        if k in self.assertion_keys:
            self._generate_key()
        return k

    def _generate_param_key(self):
        k = os.urandom(3).hex()
        if k in self.param_keys:
            self._generate_param_key()
        return k

    def _parse_schema(self, schema):
        # If schema is a reference
        d = {}
        components = self.parserobj.components
        vmap = self.parserobj.variables
        dtypes = self.parserobj.data_types
        if "$ref" in schema["schema"]:
            ref = schema["schema"]["$ref"]
            key = None
            s = components["schemas"]
            for k in s.keys():
                if ref.endswith(k):
                    key = k
                    break
            d = s[key]
        else:
            d = schema["schema"]
        try:
            if d["type"] == "object":
                properties = d["properties"]
                if isinstance(properties, dict):
                    for key, value in properties.items():
                        try:
                            if value["type"] in dtypes:
                                v = "{}_body_{}".format(self.testid, key)
                                vmap[v] = self._generate_sample_data(
                                    value["type"], self.testid
                                )
                                self.body_params.append(
                                    {
                                        "key": self._generate_param_key(),
                                        "name": key,
                                        "dataType": value["type"],
                                        "variableKey": v,
                                    }
                                )
                        except KeyError:
                            pass
        except KeyError:
            pass

    def _parse_response_schema(self, respcode, schema):
        properties = schema["properties"]
        if isinstance(properties, dict):
            for k, v in properties.items():
                key = self._generate_key()
                # Add code and label
                assertion = {
                    "name": "",
                    "label": "",
                    "code": "",
                    "field": "",
                    "operator": "",
                    "value": "",
                }
                assertion["key"] = key
                assertion["name"] = respcode
                assertion["field"] = "body_{}".format(k)
                assertion["operator"] = "equal"
                assertion["value"] = v["type"]
                assertion[
                    "label"
                ] = "For {} the response body {} must be of type {}".format(
                    respcode, k, v["type"]
                )
                # dv = "_dynamic_{}_{}_body_{}_{}".format(tid, respcode, k, v['type'])
                # dvars.append({"label": "{} body {}".format(respcode, k), "key": dv})
                self.assertions.append(assertion)

    def _generate_response_assertions(self, respcode, responses):
        try:
            respdata = responses[respcode]
            component_map = self.parserobj.component_map
            if "content" in respdata:
                content = respdata["content"]
                if "application/json" in content:
                    # Add code and label
                    key = self._generate_key()
                    self.assertions.append(
                        {
                            "key": key,
                            "name": respcode,
                            "field": "contentType",
                            "operator": "equal",
                            "value": "application/json",
                            "label": "For {} the content type must be {}".format(
                                respcode, "application/json"
                            ),
                        }
                    )
                    schema = content["application/json"]["schema"]
                    if "$ref" in schema:
                        try:
                            schema_data = component_map[schema["$ref"]]
                            self._parse_response_schema(respcode, schema_data)
                        except KeyError:
                            pass
                    if schema["type"] == "object":
                        self._parse_response_schema(respcode, schema)
        except KeyError as e:
            pass

    def _generate_assertions(self):
        responses = self.method_data["responses"]
        if responses:
            codes = list(responses.keys())  # -> ['200', '401, '403']
            if codes:
                response_codes = codes
                key = self._generate_key()
                if len(codes) > 1:
                    self.assertions.append(
                        {
                            "key": key,
                            "name": "statusCode",
                            "label": "Status code must be one of {}".format(codes),
                            "operator": "member",
                            "value": json.dumps(codes),
                            "field": "statusCode",
                        }
                    )
                if len(codes) == 1:
                    self.assertions.append(
                        {
                            "key": key,
                            "name": "statusCode",
                            "label": "Status code must be equal to {}".format(codes[0]),
                            "operator": "equal",
                            "value": codes[0],
                            "field": "statusCode",
                        }
                    )
                for c in codes:
                    # Generate assertions for each response type
                    self.assertion_code_list.append(c)
                    self._generate_response_assertions(c, responses)

    def _generate_body_params(self):
        request_bodies = self.method_data.get("requestBody", None)
        if request_bodies:
            try:
                content = request_bodies["content"]
                s = content["application/json"]
                self._parse_schema(s)
                self.body_content_type = "application/json"
                self.is_body = True
            except KeyError:
                pass

    def _generate_params(self):
        params = self.method_data.get("parameters", None)
        vmap = {}
        if isinstance(params, list):
            for p in params:
                try:
                    name = p["name"]
                    key = self._generate_param_key()
                    tid = self.testid
                    if p["in"] == "path":
                        vkey = "{}_path_{}".format(tid, name)
                        self.path_params.append(
                            {
                                "key": key,
                                "name": name,
                                "dataType": "string",
                                "variableKey": vkey,
                            }
                        )
                        vmap[vkey] = self._generate_sample_data("string", tid)
                    if p["in"] == "query":
                        vkey = "{}_query_{}".format(tid, name)
                        self.query_params.append(
                            {
                                "key": key,
                                "name": name,
                                "dataType": "string",
                                "variableKey": vkey,
                            }
                        )
                        vmap[vkey] = self._generate_sample_data("string", tid)
                    if p["in"] == "header":
                        vkey = "{}_header_{}".format(tid, name)
                        self.header_params.append(
                            {
                                "key": key,
                                "name": name,
                                "dataType": "string",
                                "variableKey": vkey,
                            }
                        )
                        vmap[vkey] = self._generate_sample_data("string", tid)
                except KeyError:
                    pass
        self.parserobj.variables.update(vmap)

    def generate(self):
        self._generate_params()
        self._generate_body_params()
        self._generate_assertions()
        return self


class Parser(object):
    def __init__(self, data={}):
        self.data = data
        # OpenAPI specific data types.
        self.data_types = ["string", "integer", "array", "object", "boolean"]
        # Methods we are looking for.
        self.methods = ["get", "put", "post", "patch", "delete"]
        self.variables = {}
        self.dynamic_variables = {}
        self.testids = []
        self.components = []
        # placeholder for tests
        self.tests = []
        self.servers = {}

    def _generate_testid(self):
        i = os.urandom(2).hex().upper()
        if i in self.testids:
            self._generate_testid()
        self.testids.append(i)
        return i

    def _extract_servers(self):
        try:
            for s in self.data["servers"]:
                self.servers.update({s["description"]: s["url"]})
        except KeyError:
            pass

    def _build_component_tree(self):
        pass

    def _generate_method_test(self, test_id, method_data):
        method = Method(self, test_id, method_data)
        method.generate()
        return method

    def _generate_path_test(self, path, path_data):
        # Find what methods are given in the path
        methods_in_path = {}
        for m in self.methods:
            try:
                methods_in_path[m] = path_data[m]
            except KeyError:
                pass
        for method, method_data in methods_in_path.items():
            test = {"pathName": path}
            test_id = self._generate_testid()
            test["testId"] = test_id
            test["methodName"] = method
            mt = self._generate_method_test(test_id, method_data)
            # mt = method(data[m], test_id, components, variables, dynamic_variables, testids)
            test["assertions"] = mt.assertions
            test["assertionCodes"] = json.dumps(mt.assertion_codes)
            test["assertionCodeList"] = json.dumps(mt.assertion_code_list)
            test["bodyContentType"] = json.dumps(mt.body_content_type)
            test["isBody"] = mt.is_body
            test["bodyParams"] = mt.body_params
            test["headerParams"] = mt.header_params
            test["pathParams"] = mt.path_params
            test["queryParams"] = mt.query_params
            # test["requestParams"] = json.dumps(mt.request_params)
            # test["dynamicVars"] = mt['dynamicVars']
            # test["dynamicVars"] = json.dumps(mt['dynamicVars'])
            # test_list.append(test)
            self.tests.append(test)

    def is_valid(self):
        paths = self.data["paths"]
        if paths:
            return True
        return False

    def generate(self):
        paths = self.data["paths"]
        self.components = self.data["components"]
        self.component_map = {}
        for k in self.components.keys():
            v = self.components[k]
            for inner in v.keys():
                key = "#/components/{}/{}".format(k, inner)
                self.component_map[key] = v[inner]
        for path, path_data in paths.items():
            self._generate_path_test(path, path_data)
        self._extract_servers()
        return self.tests


def generate(data):
    d = yaml.load(data, yaml.Loader)
    p = Parser(data=d)
    if not p.is_valid():
        return {"error": True}
    p.generate()
    return {"error": False, "parser": p}


if __name__ == "__main__":
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    with open("banking.yml", "r") as f:
        resp = generate(f.read())
        for item in resp.tests:
            print(item)
