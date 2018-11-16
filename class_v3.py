#classes used definition
class legit_combo:
    def __init__(self,ip,geo,time,method,username):
        self.ip = ip
        self.geo = geo
        self.time = time
        self.method = method
        self.user = username 
    def detail(self):
        a = "user: %s, time: %s, ip: %s, geo: %s, method: %s"%(self.user,self.time,self.ip,self.geo,self.method)
        return(a)

class invalid_combo:
    def __init__(self,name,geo,time,ip):
        self.ip = ip 
        self.user = name
        self.geo = geo
        self.time= time
    def detail(self):
        a = "time: %s, geo: %s, ip: %s, name: %s"%(self.time,self.geo,self.ip,self.user)
        return(a)

class failed_combo:
    def __init__(self,geo,time,method,ip,name):
        self.geo = geo
        self.time = time
        self.method = method
        self.ip = ip
        self.user = name 
    def detail(self):
        a = "time: %s, geo: %s, method: %s,ip:%s"%(self.time,self.geo,self.method,self.ip)
        return(a)