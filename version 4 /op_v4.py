import sqlite3

from class_v4 import legit_combo
from class_v4 import invalid_combo
from class_v4 import failed_combo
import filter_v4 as f

# check if exist in whitelist database 
def isitin(ip):
    conn = sqlite3.connect('whitelist.db')
    c = conn.cursor()
    with conn:
        c.execute('SELECT ip FROM whitelist WHERE ip = :ip',{'ip':ip})
    data = c.fetchall()
    conn.close()
    if len(data) == 0:
        return 0
    else:
        return 1

# operations needed for usage of database 
def update_success(com):
        conn = sqlite3.connect('rsuc.db')
        c = conn.cursor()
        # see if existing 
        c.execute("SELECT ip,hostname from success_logins WHERE ip = :ip AND hostname = :host",{'ip':com.ip,'host':com.user})
        data = c.fetchall()
        # does not exits 
        if len(data) == 0:
                #insert new entry 
                with conn:
                        c.execute("INSERT INTO success_logins VALUES (:hostname,:ip,:date,:geo,:method)",{'hostname':com.user,'ip':com.ip,'date':com.time,'geo':com.geo,'method':com.method}) 
                conn.commit()
                conn.close()
                conn = sqlite3.connect('firstspotted.db')
                c = conn.cursor()
                with conn:
                        c.execute("INSERT INTO fir VALUES (:ip,:username,:time,:state)",{'ip':com.ip,'username':com.user,'time':com.time,'state':"successful"})
                conn.commit()
                conn.close()
                #f.check_for_whitelist(com.ip)
        else:
                #update current entry 
                c.execute("""UPDATE success_logins
                        SET datetime = :date,
                            geolocation = :geo,
                            method = :m
                        WHERE ip = :ip AND hostname = :host""",{'date':com.time,'geo':com.geo,'m':com.method,'ip':com.ip,'host':com.user})
                conn.commit()
                conn.close()

# check if existing in invalid, if it does, increment the count and other info 
# if not, create a new entry 
def update_invalid(com):
        conn = sqlite3.connect('rinva.db')
        c = conn.cursor()
        # see if existing 
        c.execute("SELECT ip FROM invalid_logins WHERE ip = :ip AND hostname = :host",{'ip':com.ip,'host':com.user})
        data = c.fetchall()
        if len(data) == 0:
                # insert a new entry 
                with conn:
                        c.execute("INSERT INTO invalid_logins VALUES (:hostname,:ip,:geo,:date,:count)",{'hostname':com.user,'ip':com.ip,'geo':com.geo,'date':com.time,'count':1})
                conn.commit()
                conn.close()
                conn = sqlite3.connect('firstspotted.db')
                c = conn.cursor()
                with conn:
                        c.execute("INSERT INTO fir VALUES (:ip,:hostname,:time,:state)",{'ip':com.ip,'hostname':com.user,'time':com.time,'state':"Invalid"})
                conn.commit()
                conn.close()
                #f.check_for_whitelist(com.ip)

        else:
                #uppdate the currrent existing entry 
                with conn:
                        c.execute("""UPDATE invalid_logins
                        SET geolocation = :geo,
                            datatime = :time,
                            count = count+1
                        WHERE ip = :ip AND hostname = :host""",{'geo':com.geo,'time':com.time,'ip':com.ip,'host':com.user})
                c.execute("SELECT count from invalid_logins WHERE ip = :ip AND hostname = :host",{'ip':com.ip,'host':com.user})
                data = c.fetchall()
                conn.commit()
                conn.close()
                # if the current one is beyound the threshold 
                #print(data[0][0])
                if data[0][0] > 5: #sub 5 with threshold
                        # check if in the whitelist 
                        th = data[0][0]
                        tmp = f.check_for_whitelist(com.ip)
                        if tmp ==0:
                            # means not in the whitelist 
                            conn = sqlite3.connect('watchlist.db')
                            c = conn.cursor()
                            # find if exist already 
                            c.execute("SELECT ip from watchlist WHERE ip = :ip AND hostname = :host",{'ip':com.ip,'host':com.user})
                            data = c.fetchall()
                            if len(data) == 0:
                                with conn:
                                    c.execute("INSERT INTO watchlist VALUES (:ip,:hostname,:geo,:date,:count,:method)",{'ip':com.ip,'hostname':com.user,'geo':com.geo,'date':com.time,'count':th,'method':'unknown'}) 
                                conn.commit()
                                conn.close()    
                            else:
                                with conn:
                                    c.execute("""UPDATE watchlist
                                            SET geolocation = :geo,
                                                datatime = :time,
                                                count = count + 1
                                            WHERE ip = :ip AND hostname = :host""",{'geo':com.geo,'time':com.time,'ip':com.ip,'host':com.user} )
                                conn.commit()
                                conn.close()


def update_failed(com):
        conn = sqlite3.connect('rf.db')
        c = conn.cursor()
        # see if existing 
        c.execute("SELECT ip from failed_logins WHERE ip = :ip AND hostname = :host",{'ip':com.ip,'host':com.user})
        data = c.fetchall()
        # does not exist 
        if len(data) == 0:
                #create new entry 
                with conn:
                        c.execute("INSERT INTO failed_logins VALUES (:hostname,:ip,:geo,:method,:date,:count)",{'hostname':com.user,'ip':com.ip,'geo':com.geo,'method':com.method,'date':com.time,'count':0})
                conn.commit()
                conn.close()
                conn = sqlite3.connect('firstspotted.db')
                c = conn.cursor()
                with conn:
                        c.execute("INSERT INTO fir VALUES (:ip,:hostname,:time,:state)",{'ip':com.ip,'hostname':com.user,'time':com.time,'state':"FAILED"})
                conn.commit()
                conn.close()
                #f.check_for_whitelist(com.ip)
        else:
                #update the extry 
                with conn:
                        c.execute("""UPDATE failed_logins
                        SET geoloctaion = :geo,
                            method = :m,
                            datatime = :time,
                            count = count + 1
                        WHERE ip = :ip AND hostname = :host""",{'geo':com.geo,'m':com.method,'time':com.time,'ip':com.ip,'host':com.user}
                            )
                c.execute("SELECT count from failed_logins WHERE ip = :ip AND hostname = :host",{'ip':com.ip,'host':com.user})
                data = c.fetchall()
                conn.commit()
                conn.close()
                # check if existing 
                if data[0][0] > 5:
                        th = data[0][0]
                        tmp = f.check_for_whitelist(com.ip)
                        if tmp ==0:
                            # does not whitelisted 
                            conn = sqlite3.connect('watchlist.db')
                            c = conn.cursor()
                            c.execute("SELECT ip from watchlist WHERE ip = :ip AND hostname = :host",{'ip':com.ip,'host':com.user})
                            data = c.fetchall()
                            if len(data) == 0:
                                    # add entry to the watch list 
                                    with conn:
                                           c.execute("INSERT INTO watchlist VALUES (:ip,:hostname,:geo,:date,:count,:method)",{'ip':com.ip,'hostname':com.user,'geo':com.geo,'date':com.time,'count':th,'method':com.method})
                            else:
                                    with conn:
                                            c.execute("""UPDATE watchlist
                                            SET geolocation = :geo,
                                                datatime = :time,
                                                count = count + 1,
                                                method = :m
                                            WHERE ip = :ip AND hostname = :host""",{'geo':com.geo,'time':com.time,'m':com.method,'ip':com.ip,'host':com.user})
                            conn.commit()
                            conn.close()


# def insert_whitelist(ip):
#         conn = sqlite3.connect('whitelist.db')
#         c = conn.cursor()
#         with conn:
#                 c.execute("INSERT INTO whitelist VALUES (:ip)",{'ip':ip})
#         conn.commit()
#         conn.close()

# print out to check if work properly
def check_first():
        conn = sqlite3.connect('firstspotted.db')
        c = conn.cursor()
        c.execute("SELECT ip, hostname,time,state from fir")
        data = c.fetchall()
        for i in data:
                print(i)
        conn.close()

def check_succ():
        conn = sqlite3.connect('rsuc.db')
        c = conn.cursor()
        c.execute("SELECT ip, hostname, datetime,geolocation,method from success_logins")
        data = c.fetchall()
        for i in data:
                print(i)
        conn.close()

def check_in():
        conn = sqlite3.connect('rinva.db')
        c = conn.cursor()
        c.execute("SELECT ip, hostname, datatime,geolocation,count from invalid_logins")
        data = c.fetchall()
        for i in data:
                print(i)
        conn.close()

def check_f():
        conn = sqlite3.connect('rf.db')
        c = conn.cursor()
        c.execute("SELECT ip, hostname, datatime,geoloctaion,method,count from failed_logins")
        data = c.fetchall()
        for i in data:
                print(i)
        conn.close()

def check_w():
        conn = sqlite3.connect('whitelist.db')
        c = conn.cursor()
        c.execute("SELECT ip from whitelist")
        data = c.fetchall()
        for i in data:
                print(i)
        conn.close()

def check_wa():
        conn = sqlite3.connect('watchlist.db')
        c = conn.cursor()
        c.execute("SELECT ip,hostname,geolocation,datatime,count,method from watchlist")
        data = c.fetchall()
        for i in data:
                print(i)
        conn.close()    