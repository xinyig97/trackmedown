# delete entry from watchlist 
# should or should not reset the count = 0?  
import sqlite3
import op_v3 as o
import output as ou
def remove_from_watchlist(ip,name):
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    with conn:
        c.execute('SELECT * FROM watchlist WHERE ip = :ip  AND  hostname = :user',{'ip':ip,'user':name})
        data = c.fetchall()
        if len(data) == 0:
            res = input("no such data, do you want to exit or reset? reply 'exit' or 'reset' ") 
            if res == 'reset':
                ip = input('what is the ip that you do not need to watch anymore? ')
                name = input('what is the corresponding username :')
                remove_from_watchlist(ip,name)
            else:
                print('ok, bye')
        else:
            print(data)
            action = input("are you certain that you do not need to watch this guy anymore? reply 'yes' or 'no' ")
            if action == 'yes':
                c.execute('DELETE FROM watchlist WHERE ip = :ip AND hostname = :user',{'ip':ip,'user':name})
            print('you are all set! :D')
    conn.commit()
    conn.close()
    return

def reset_count(ip,name):
    conn = sqlite3.connect('rinva.db')
    c = conn.cursor()
    with conn:
        c.execute('SELECT * FROM invalid_logins WHERE ip = :ip AND hostname = :user',{'ip':ip,'user':name})
        data = c.fetchall()
        if len(data) != 0:
            c.execute('''UPDATE invalid_logins
            SET count = 0
            WHERE ip = :ip AND hostname = :user''',{'ip':ip,'user':name})
    conn.commit()
    conn.close()
    conn = sqlite3.connect('rf.db')
    c = conn.cursor()
    with conn:
        c.execute('SELECT * FROM failed_logins WHERE ip = :ip AND hostname = :user',{'ip':ip,'user':name})
        data = c.fetchall()
        if len(data) != 0:
            c.execute('''UPDATE failed_logins
            SET count = 0
            WHERE ip = :ip AND hostname = :user''',{'ip':ip,'user':name})
    conn.commit()
    conn.close()



# q1 = input("do you want to delete anything from the watchlist? reply 'yes' or 'no' ")
# if q1 == 'yes':
#     ip = input('what is the ip that you dont need to watchlist: ')
#     name = input('what is the corresponding username: ')
#     remove_from_watchlist(ip,name)
#     q2 = input("do you want to reset the count of this entry? reply 'yes' or 'no' ")
#     if q2 == 'yes':
#         reset_count(ip,name)
#         print('you are all set')
#     else:
#         print('fine')
#     ou.output_watchlist()

# else:
#     print('ok bye')


# print('check invalid')
# o.check_in()
# print('check f')
# o.check_f()