import sqlite3
from classes import legit_combo
from classes import invalid_combo
from classes import failed_combo

# operations needed for usage of database 

def insert_success(key,suc):
        conn = sqlite3.connect('success.db')
        c = conn.cursor()
        with conn : 
                c.execute("INSERT INTO successful_logins VALUES (:hostname,:ip,:date,:geo,:method)",{'hostname':key,'ip':suc.ip,'date':suc.time,'geo':suc.geo,'method':suc.method}) 
        conn.commit()
        conn.close()


def insert_invalid(k,inc):
        conn = sqlite3.connect('invalid.db')
        c = conn.cursor()
        with conn : 
                c.execute("INSERT INTO invalid_logins VALUES (:ip,:date,:geo,:hostname)",{'ip':k,'date':inc.time,'geo':inc.geo,'hostname':inc.name})
        conn.commit()
        conn.close()

def insert_failed(k,fa):
        conn = sqlite3.connect('failed.db')
        c = conn.cursor()
        with conn:
                c.execute("INSERT INTO failed_logins VALUES (:ip,:date,:geo,:method)",{'ip':k,'date':fa.time,'geo':fa.geo,'method':fa.method})
        conn.commit()
        conn.close()

def insert_whitelist(k,suc):
        conn = sqlite3.connect('whitelist.db')
        c = conn.cursor()
        with conn:
                c.execute("INSERT INTO white_listed VALUES (:hostname,:ip)",{'hostname':k,'ip':suc.ip})
        conn.commit()
        conn.close()

def insert_watchlist_i(k,inc):
        conn = sqlite3.connect('watchlist.db')
        c = conn.cursor()
        with conn :
                c.execute("INSERT INTO watch_listed VALUES (:ip)",{'ip':inc.ip})
        conn.commit()
        conn.close()

def insert_watchlist_f(k,fa):
        conn = sqlite3.connect('watchlist.db')
        c = conn.cursor()
        with conn:
                c.execute("INSERT INTO watch_listed VALUES (:ip)",{'ip':fa})
        conn.commit()
        conn.close()

def search_in_watchedl(w,a):
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()

    c.execute('''SELECT ip FROM watch_listed WHERE ip = :ip''',{'ip':w})
    data = c.fetchall()
    if len(data) == 0:
        a = 0
        print('not in alert immediately, dwdw')
    else:
        a = 1
        print('alert now!!!')
    conn.close()

def search_in_whitel(hn,w,a):
    conn = sqlite3.connect('whitelist.db')
    c = conn.cursor()

    c.execute('''SELECT hostname,ip FROM white_listed WHERE hostname = :hostname AND ip = :ip''',{'hostname':hn,'ip':w})
    data  = c.fetchall()
    if len(data) == 0:
        a = 0
        print('not existing in whitelist')
    else:
        a = 1
        print('should be whitelisted already. move on')
    conn.close()
    