import yaml
from pprint import pprint 

class Dict_handler():
    def __init__(self,yaml_file:str) -> None:
        self.dict = {}
        self.file = yaml_file

    def yaml_reader(self):
        yfile = open(self.file,"r")
        self.dict = yaml.safe_load(yfile)
        yfile.close()
    
class Info_yaml(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[1]]
        return self.data

    def api_title(self):
        self.data = self.dict[self.list1[1]]
        self.title = self.data['title']
        return self.title
 
    def api_desc(self):
        self.data = self.dict[self.list1[1]]
        self.description = self.data['description']
        return self.description
        
    def api_version(self):
        self.data = self.dict[self.list1[1]]
        self.version = self.data['version']
        return self.version
    
class Servers_yaml(Info_yaml):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        return self.list1
    
    def data(self):
        self.data = self.dict[self.list1[2]]
        return self.data
    
    def url_server(self):
        self.data = self.dict[self.list1[2]][0]
        self.url = self.data['url']
        return self.url
    
    def desc_server(self):
        self.data = self.dict[self.list1[2]][0]
        self.desc = self.data['description']
        return self.desc
    
class Paths_yaml(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[3]]
        return self.data
    
class Accounts_get(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[3]]
        self.accounts = self.data['/accounts']['get']
        return self.accounts
    
    def summary_get(self):
        self.data = self.dict[self.list1[3]]['/accounts']['get']['summary']
        return self.data
    
    def description_get(self):
        self.data = self.dict[self.list1[3]]['/accounts']['get']['description']
        return self.data

    def operationId_get(self):
        self.data = self.dict[self.list1[3]]['/accounts']['get']['operationId']
        return self.data

    def parameters_get(self):
        self.data = self.dict[self.list1[3]]['/accounts']['get']['parameters']
        return self.data
    
    def responses_get(self):
        self.data = self.dict[self.list1[3]]['/accounts']['get']['responses']
        return self.data      

class Accounts_post(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[3]]
        self.accounts = self.data['/accounts']['post']
        return self.accounts
    
    def summary_post(self):
        self.data = self.dict[self.list1[3]]['/accounts']['post']['summary']
        return self.data
    
    def description_post(self):
        self.data = self.dict[self.list1[3]]['/accounts']['post']['description']
        return self.data

    def operationId_post(self):
        self.data = self.dict[self.list1[3]]['/accounts']['post']['operationId']
        return self.data

    def parameters_post(self):
        self.data = self.dict[self.list1[3]]['/accounts']['post']['parameters']
        return self.data

    def requestbody_post(self):
        self.data = self.dict[self.list1[3]]['/accounts']['post']['requestBody']
        return self.data    

    def responses_post(self):
        self.data = self.dict[self.list1[3]]['/accounts']['post']['responses']
        return self.data    

class AccountId_get(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[3]]
        self.accounts = self.data["/accounts/{accountId}"]['get']
        return self.accounts
    
    def summary_get(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['get']['summary']
        return self.data
    
    def description_get(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['get']['description']
        return self.data

    def operationId_get(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['get']['operationId']
        return self.data

    def parameters_get(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['get']['parameters']
        return self.data
    
    def responses_get(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['get']['responses']
        return self.data      

class Accounts_put(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[3]]
        self.accounts = self.data['/accounts/{accountId}']['put']
        return self.accounts
    
    def summary_put(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['put']['summary']
        return self.data
    
    def description_put(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['put']['description']
        return self.data

    def operationId_put(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['put']['operationId']
        return self.data

    def parameters_put(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['put']['parameters']
        return self.data

    def requestbody_put(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['put']['requestBody']
        return self.data    

    def responses_put(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['put']['responses']
        return self.data  

class AccountId_delete(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[3]]
        self.accounts = self.data["/accounts/{accountId}"]['delete']
        return self.accounts
    
    def summary_delete(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['delete']['summary']
        return self.data
    
    def description_delete(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['delete']['description']
        return self.data

    def operationId_delete(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['delete']['operationId']
        return self.data

    def parameters_delete(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['delete']['parameters']
        return self.data
    
    def responses_delete(self):
        self.data = self.dict[self.list1[3]]['/accounts/{accountId}']['delete']['responses']
        return self.data    

class Transfers_get(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[3]]
        self.accounts = self.data['/transfers']['get']
        return self.accounts
    
    def summary_get(self):
        self.data = self.dict[self.list1[3]]['/transfers']['get']['summary']
        return self.data
    
    def description_get(self):
        self.data = self.dict[self.list1[3]]['/transfers']['get']['description']
        return self.data

    def operationId_get(self):
        self.data = self.dict[self.list1[3]]['/transfers']['get']['operationId']
        return self.data

    def parameters_get(self):
        self.data = self.dict[self.list1[3]]['/transfers']['get']['parameters']
        return self.data
    
    def responses_get(self):
        self.data = self.dict[self.list1[3]]['/transfers']['get']['responses']
        return self.data      

class Transfers_post(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[3]]
        self.accounts = self.data['/transfers']['post']
        return self.accounts
    
    def summary_post(self):
        self.data = self.dict[self.list1[3]]['/transfers']['post']['summary']
        return self.data
    
    def description_post(self):
        self.data = self.dict[self.list1[3]]['/transfers']['post']['description']
        return self.data

    def operationId_post(self):
        self.data = self.dict[self.list1[3]]['/transfers']['post']['operationId']
        return self.data

    def parameters_post(self):
        self.data = self.dict[self.list1[3]]['/transfers']['post']['parameters']
        return self.data  

    def responses_post(self):
        self.data = self.dict[self.list1[3]]['/transfers']['post']['responses']
        return self.data    

class Balances_get(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[3]]
        self.accounts = self.data['/balances']['get']
        return self.accounts
    
    def summary_get(self):
        self.data = self.dict[self.list1[3]]['/balances']['get']['summary']
        return self.data
    
    def description_get(self):
        self.data = self.dict[self.list1[3]]['/balances']['get']['description']
        return self.data

    def operationId_get(self):
        self.data = self.dict[self.list1[3]]['/balances']['get']['operationId']
        return self.data

    def parameters_get(self):
        self.data = self.dict[self.list1[3]]['/balances']['get']['parameters']
        return self.data
    
    def responses_get(self):
        self.data = self.dict[self.list1[3]]['/balances']['get']['responses']
        return self.data 

class Components_yaml(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[4]]['schemas']
        return self.data

class Schemas_account(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[4]]['schemas']['Account']
        return self.data
    
    def type_account(self):
        self.data = self.dict[self.list1[4]]['schemas']['Account']['type']
        return self.data

    def Properties_account(self):
        self.data = self.dict[self.list1[4]]['schemas']['Account']['properties']
        return self.data

    def required_account(self):
        self.data = self.dict[self.list1[4]]['schemas']['Account']['required']
        return self.data

class Schemas_transfer(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[4]]['schemas']['Transfer']
        return self.data

    def type_transfer(self):
        self.data = self.dict[self.list1[4]]['schemas']['Transfer']['type']
        return self.data

    def Properties_transfer(self):
        self.data = self.dict[self.list1[4]]['schemas']['Transfer']['properties']
        return self.data

    def required_transfer(self):
        self.data = self.dict[self.list1[4]]['schemas']['Transfer']['required']
        return self.data

class Schemas_balance(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[4]]['schemas']['Balance']
        return self.data

    def type_balance(self):
        self.data = self.dict[self.list1[4]]['schemas']['Balance']['type']
        return self.data

    def Properties_balance(self):
        self.data = self.dict[self.list1[4]]['schemas']['Balance']['properties']
        return self.data

    def required_balance(self):
        self.data = self.dict[self.list1[4]]['schemas']['Balance']['required']
        return self.data
    
class Schemas_error(Dict_handler):
    def info(self):
        self.list1 = []
        for i in self.dict:
            self.list1.append(i)
        self.data = self.dict[self.list1[4]]['schemas']['Error']
        return self.data

    def type_error(self):
        self.data = self.dict[self.list1[4]]['schemas']['Error']['type']
        return self.data

    def Properties_error(self):
        self.data = self.dict[self.list1[4]]['schemas']['Error']['properties']
        return self.data

    def required_error(self):
        self.data = self.dict[self.list1[4]]['schemas']['Error']['required']
        return self.data


data1 = Dict_handler("banking.yml")
data1.yaml_reader()

data2 = Info_yaml("banking.yml")
data2.yaml_reader()
data2.info()
print(data2.api_title())
print(data2.api_desc())
print(data2.api_version())

data3 = Servers_yaml('banking.yml')
data3.yaml_reader()
data3.info()
print(data3.url_server())
print(data3.desc_server())

data4 = Paths_yaml('banking.yml')
data4.yaml_reader()
data4.info()

data5 = Accounts_get("banking.yml")
data5.yaml_reader()
data5.info()
print(data5.summary_get())
print(data5.description_get())
print(data5.operationId_get())
print(data5.parameters_get())
print(data5.responses_get())

data6 = Accounts_post('banking.yml')
data6.yaml_reader()
data6.info()
print(data6.summary_post())
print(data6.description_post())
print(data6.operationId_post())
print(data6.parameters_post())
print(data6.requestbody_post())
print(data6.responses_post())


data7 = AccountId_get('banking.yml')
data7.yaml_reader()
data7.info()
print(data7.summary_get())
print(data7.description_get())
print(data7.operationId_get())
print(data7.parameters_get())
print(data7.responses_get())


data8 = Accounts_put('banking.yml')
data8.yaml_reader()
data8.info()
print(data8.summary_put())
print(data8.description_put())
print(data8.operationId_put())
print(data8.parameters_put())
print(data8.requestbody_put())
print(data8.responses_put())


data9 = AccountId_delete('banking.yml')
data9.yaml_reader()
data9.info()
print(data9.summary_delete())
print(data9.description_delete())
print(data9.operationId_delete())
print(data9.parameters_delete())
print(data9.responses_delete())

data10 = Transfers_get("banking.yml")
data10.yaml_reader()
data10.info()
print(data10.summary_get())
print(data10.description_get())
print(data10.operationId_get())
print(data10.parameters_get())
print(data10.responses_get())


data11 = Transfers_post('banking.yml')
data11.yaml_reader()
data11.info()
print(data11.summary_post())
print(data11.description_post())
print(data11.operationId_post())
print(data11.parameters_post())
print(data11.responses_post())

data12 = Balances_get("banking.yml")
data12.yaml_reader()
data12.info()
print(data12.summary_get())
print(data12.description_get())
print(data12.operationId_get())
print(data12.parameters_get())
print(data12.responses_get())

data13 = Components_yaml('banking.yml')
data13.yaml_reader()
print(data13.info())

data14 = Schemas_account('banking.yml')
data14.yaml_reader()
data14.info()
print(data14.type_account())
print(data14.Properties_account())
print(data14.required_account())

data15 = Schemas_transfer('banking.yml')
data15.yaml_reader()
data15.info()
print(data15.type_transfer())
print(data15.Properties_transfer())
print(data15.required_transfer())

data16 = Schemas_balance('banking.yml')
data16.yaml_reader()
data16.info()
print(data16.type_balance())
print(data16.Properties_balance())
print(data16.required_balance())

data17 = Schemas_error('banking.yml')
data17.yaml_reader()
data17.info()
print(data17.type_error())
print(data17.Properties_error())
print(data17.required_error())

