import sqlite3
from class_v3 import legit_combo
from class_v3 import invalid_combo
from class_v3 import failed_combo

conn  =sqlite3.connect('rsuc.db')
c = conn.cursor()
c.execute("""CREATE TABLE success_logins(
    hostname text,
    ip text,
    datetime text,
    geolocation text,
    method text
)""")
conn.close()
# can actually include a counter 
conn = sqlite3.connect('rinva.db')
c = conn.cursor()
c.execute("""CREATE TABLE invalid_logins(
    hostname text,
    ip text,
    geolocation text,
    datatime text,
    count integer
)""")
conn.close()

conn = sqlite3.connect('rf.db')
c = conn.cursor()
c.execute("""CREATE TABLE failed_logins(
    hostname text,
    ip text,
    geoloctaion text,
    method text,
    datatime text,
    count integer
)""")
conn.close()

conn = sqlite3.connect('whitelist.db')
c = conn.cursor()
c.execute("""CREATE TABLE whitelist(
    ip text
)""")
conn.close()

conn = sqlite3.connect('watchlist.db')
c = conn.cursor()
c.execute("""CREATE TABLE watchlist(
    ip text,
    hostname text,
    geolocation text,
    datatime text,
    count integer,
    method text
)""")
conn.close()

conn = sqlite3.connect('firstspotted.db')
c = conn.cursor()
c.execute("""CREATE TABLE fir(
    ip text,
    hostname text,
    time text,
    state text
)""")
conn.close()

