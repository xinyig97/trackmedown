#classes used definition
class legit_combo:
    def __init__(self,ip,geo,time,method):
        self.ip = ip
        self.geo = geo
        self.time = time
        self.method = method
    def detail(self):
        a = "time: %s, ip: %s, geo: %s, method: %s"%(self.time,self.ip,self.geo,self.method)
        return(a)

class invalid_combo:
    def __init__(self,name,geo,time):
        self.name = name
        self.geo = geo
        self.time= time
    def detail(self):
        a = "time: %s, geo: %s, name: %s"%(self.time,self.geo,self.name)
        return(a)

class failed_combo:
    def __init__(self,geo,time,method):
        self.geo = geo
        self.time = time
        self.method = method
    def detail(self):
        a = "time: %s, geo: %s, method: %s"%(self.time,self.geo,self.method)
        return(a)