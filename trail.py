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
        return self.list1
    
    def data(self):
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
        return self.list1
    
    def data(self):
        self.data = self.dict[self.list1[3]]
        return self.data
    
    class Accounts:
        def info(self):
            self.list1 = []
            for i in self.dict:
                self.list1.append(i)
            return self.list1
        
        # def data_account(self):





data1 = Dict_handler("banking.yml")
data1.yaml_reader()

data2 = Info_yaml("banking.yml")
data2.yaml_reader()
data2.info()
print(data2.data())
print(data2.api_title())
print(data2.api_desc())
print(data2.api_version())

data3 = Servers_yaml('banking.yml')
data3.yaml_reader()
data3.info()
print(data3.data())
print(data3.url_server())
print(data3.desc_server())

data4 = Paths_yaml('banking.yml')
data4.yaml_reader()
data4.info()
pprint(data4.data())




    

