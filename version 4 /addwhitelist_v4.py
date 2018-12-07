# manually insert specific whitlised ip
import sqlite3

def add_whi(ip):
    conn = sqlite3.connect('whitelist.db')
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO whitelist VALUES (:ip)",{'ip':ip})
    conn.commit()
    conn.close()

# inp = input('what is the ip that you want to whitelisted: ')
# add_whi(inp)
# print('done')
