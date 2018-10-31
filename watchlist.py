import sqlite3
# import invalid_combo from v2 
# import failed_combo from v2 

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

# create a watch list to alert immediately when a suspicious login showed up  
# either from failed attempt or from invalid ones 

conn = sqlite3.connect('watchlist.db')

c  = conn.cursor()

def insert_watched(w):
    with conn:
        c.execute("INSERT INTO watch_listed VALUES (:ip)",{'ip':w.ip})

# a is the indicator that when a suspicious login showed up that need to be alerted immediately 
def search_in_watchedl(w,a):
    c.execute('''SELECT ip FROM watch_listed WHERE ip = :ip''',{'ip':w.ip})
    data = c.fetchall()
    if len(data) == 0:
        a = 0
        print('not in alert immediately, dwdw')
    else:
        a = 1
        print('alert now!!!')
