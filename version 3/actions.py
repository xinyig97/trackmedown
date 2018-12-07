import sqlite3

def find_ip(ip):
    conn = sqlite3.connect('firstspotted.db')
    c = conn.cursor()
    with conn:
        c.execute('SELECT hostname FROM fir WHERE ip = :ip',{'ip':ip})
    data = c.fetchall()
    conn.close()
    if len(data) == 0:
        q3 = input('ip does not exist, try again? No or [ip]')
        if q3 == 'No':
            return 
        else:
            find_ip(q3)
    else:
        for i in data:
            print(i)
        q4 = input('choose your user: [User] or No')
        if q4 =='No':
            return 
        else:
            q6 = input('which scope? (successful,Invalid, FAILED')
            if q6 != 'successful' and q6 != 'Invalid' and q6 != 'FAILED':
                print('No messing around, see ya')
                return 
            else:
                resume(ip,q4,q6)



def resume(ip,q4,q6):
    conn = sqlite3.connect('firstspotted.db')
    c = conn.cursor()
    with conn:
        c.execute("SELECT ip,hostname,time,state FROM fir WHERE ip = :ip AND hostname = :host AND state = :state",{'ip':ip,'host':q4,'state':q6})
    data = c.fetchall()
    conn.close()
    if len(data) == 0:
        print('does not exist, bye')
        return 
    else:
        print('first-time spotted: ')
        for i in data:
            print(i)

        s = q6
        if s == 'successful':
            conn = sqlite3.connect('rsuc.db')
            c = conn.cursor()
            with conn:
                c.execute("SELECT ip,hostname,datetime,geolocation,method FROM success_logins WHERE ip = :ip AND hostname = :user",{'ip':ip,'user':q4})
            data = c.fetchall()
            conn.close()
            if len(data) == 0:
                print('does not exist bye')
                return 
            else:
                print('most recent spotted:(success) ')
                for i in data:
                    print(i)
                return 
        elif s == 'Invalid':
            conn = sqlite3.connect('rinva.db')
            c = conn.cursor()
            with conn:
                c.execute("SELECT hostname, ip, geolocation, datatime FROM invalid_logins WHERE ip = :ip AND hostname = :user",{'ip':ip,'user':q4})
            data = c.fetchall()
            conn.close()
            if len(data) == 0:
                print(' does not exist, bye')
                return
            else:
                print('most recent spotted:(invalid) ')
                for i in data:
                    print(i)
                return
        elif s =='FAILED':
            conn = sqlite3.connect('rf.db')
            c = conn.cursor()
            with conn:
                c.execute("SELECT ip, hostname,geoloctaion,method,datatime FROM failed_logins WHERE ip = :ip AND hostname = :user",{'ip':ip,'user':q4})
            data = c.fetchall()
            conn.close()
            if len(data) == 0:
                print('does not exist')
                return
            else:
                print('most recent spotted:(failed) ')
                for i in data:
                    print(i)
                return
