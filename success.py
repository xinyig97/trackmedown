import sqlite3
from v2 import legit_combo as suc 

conn = sqlite3.connect('success.db')

c = conn.cursor()

c.execute("""CREATE TABLE successful_logins(
    hostname text,
    ip text,
    datetime text,
    geolocation text,
    method text
)""")


def insert_success(key,suc):
    with conn:
        c.execute("INSERT INTO employees VALUES (:hostname,:ip,:logintimes,:date,:geo,:method)",{'hostname':key,'ip':suc.ip,'date':suc.time,'geo':suc.geo,'method':suc.method})











conn.commit()
conn.close()
