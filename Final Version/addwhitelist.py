# manually insert specific whitlised ip
import sqlite3

inp = input('what is the ip that you want to whitelisted: ')
conn = sqlite3.connect('whitelist.db')
c = conn.cursor()
with conn:
    c.execute("INSERT INTO whitelist VALUES (:ip)",{'ip':inp})
conn.commit()
conn.close()
print('done')

