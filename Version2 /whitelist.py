import sqlite3

class legit_combo:
    def __init__(self,ip,geo,time,method):
        self.ip = ip
        self.geo = geo
        self.time = time
        self.method = method
    def detail(self):
        a = "time: %s, ip: %s, geo: %s, method: %s"%(self.time,self.ip,self.geo,self.method)
        return(a)

# create a whitelist .db so that if a legit ip or internal ip comes in, we dont have to alert on it. 
# whitelist can be either internal or we already authenticated the id 

conn = sqlite3.connect('whitelist.db')

c = conn.cursor()

# insert an entry to the whitelist 
def insert_whitelist(hn,w):
    with conn:
        c.execute("INSERT INTO white_listed VALUES(:hostname,:ip)",{'hostname':hn,'ip':w.ip})

# a is the indicator that if an entry exist in the white list or not 
def search_in_whitel(hn,w,a):
    c.execute('''SELECT hostname,ip FROM white_listed WHERE hostname = :hostname AND ip = :ip''',{'hostname':hn,'ip':w.ip})
    data  = c.fetchall()
    if len(data) == 0:
        a = 0
        print('not existing in whitelist')
    else:
        a = 1
        print('should be whitelisted already. move on')



