import sqlite3
# initialize and create corresponding db files  
# called at initialization ONLY 
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

conn = sqlite3.connect('success.db')

c = conn.cursor()

c.execute("""CREATE TABLE successful_logins(
    hostname text,
    ip text,
    datetime text,
    geolocation text,
    method text
)""")

conn = sqlite3.connect('invalid.db')

c = conn.cursor()

c.execute("""CREATE TABLE invalid_logins (
    ip text,
    datetime text,
    geolocation text,
    hostname text
)""")

conn = sqlite3.connect('failed.db')

c = conn.cursor()

c.execute("""CREATE TABLE failed_logins(
    ip text,
    datetime text,
    geolocation text,
    method text
)""")

conn = sqlite3.connect('whitelist.db')

c = conn.cursor()

c.execute('''CREATE TABLE white_listed(
    hostname text,
    ip text
)''')

conn = sqlite3.connect('watchlist.db')

c  = conn.cursor()

c.execute('''CREATE TABLE watch_listed(
    ip test
)''')