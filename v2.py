# date : 10 - 24 - 2018
# author : xinyi guo
# UPDATE : sub excel with sqlite3 db 
# TODO : immigrate from sqlite3 db into sql 
# description : analysize log file from ssh, currently extract out successful login data and keep track of failed ones
# get geo-location of the login based on databse of maxmind : https://dev.maxmind.com/geoip/
# api: https://github.com/maxmind/GeoIP2-python
##################################################################################
# documents on notations :

# keyword one : Invalid
# Jun 17 10:56:25 ncsa-cdcx sshd[126815]: Invalid user logcheck-141.142.22.22 from 10.142.148.148
# Jun 17 10:56:25 ncsa-cdcx sshd[126815]: input_userauth_request: invalid user logcheck-141.142.22.22 [preauth]
# Jun 17 10:56:25 ncsa-cdcx sshd[126815]: Connection closed by 10.142.148.148 port 35318 [preauth]

# keyword two : Failed keybord
# Jun 17 19:20:20 ncsa-cdcx sshd[6117]: Failed keyboard-interactive/pam for invalid user root from 10.142.148.148 port 51848 ssh2
# Jun 17 19:20:20 ncsa-cdcx sshd[6117]: Connection closed by 10.142.148.148 port 51848 [preauth]

# keyword three : Accepted  - method, username, ipaddr ---> look up for geolocation
# Jun 22 13:52:05 ncsa-cdcx sshd[29643]: Accepted gssapi-with-mic for xinyig2 from 10.193.152.14 port 53193 ssh2

class legit_combo:
    def __init__(self,ip,geo,time,method):
        self.ip = ip
        self.geo = geo
        self.time = time
        self.method = method
    def detail(self):
        a = "time: %s, ip: %s, geo: %s, method: %s"%(self.time,self.ip,self.geo,self.method)
        return(a)

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
    
# gonna use regex to grab info
import re
import geoip2.database
import numpy as np
#local path to geolite2-city.mmdb database 
reader_city = geoip2.database.Reader('/Users/xinyiguo/Desktop/clean/ransome/python master/geoip_try/geoip/geoip_city/GeoLite2-City.mmdb')
# for successful user : map name to array of success_combo
success = dict()
# for invalid user: map ip to invalid combo
invalid = dict()
# for failed user : map failed to fail_combo
fail = dict()
#inp = input('feed me the log file : ')
fhand = open('file.log')
date_pattern = re.compile(r'^\S+');
suc_c = 0
in_c = 0
f_c=0
for line in fhand:
    # successful users
    if 'Accepted' in line:
        #print(line);
        suc_c = suc_c+1
        # x is the method they loggin in
        x = re.findall('Accepted (\S+)',line)
        #print(x);
        # y is their username
        y = re.findall('for (\S+)',line)
        #print(y);
        # z is their ips
        z = re.findall('from (\S+)',line)
        #print(z);
        # t is the time
        t = re.findall(date_pattern,line)
        #print(t);
        # g is the geolocation
        try:
            g = reader_city.city(z[0])
            g = g.country.iso_code
        except:
            g = 'nonfound'
        com = legit_combo(z[0],g,t[0],x[0])
        a = com.detail()
        if y[0] in success:
            success[y[0]].append(com)
        else:
            arr = list()
            success[y[0]] = arr
            success[y[0]].append(com)
    elif 'Invalid' in line:
        if('Invalid argument' in line):
            break;
        #print(line);
        in_c = in_c +1
        # y is their username
        y = re.findall('user (\S+)',line)
       # print(y);
        # z is their ips
        z = re.findall('from (\S+)',line)
        #print(z[0]);
        # t is the time
        t = re.findall(date_pattern,line)
       # print(t)
        # g is the geolocation
        try:
            g = reader_city.city(z[0])
            g = g.country.iso_code
            print(g)
           # print(g.country.iso_code);
        except:
            g = 'nonfound'
        com = invalid_combo(y[0],g,t[0])
        if z[0] in invalid:
            invalid[z[0]].append(com)
        else:
            arr = list()
            invalid[z[0]] = arr
            invalid[z[0]].append(com)
    elif 'Failed' in line:
        f_c = f_c +1
        # x is the method they loggin in
        x = re.findall('Failed (\S+)',line)
        # z is their ips
        z = re.findall('from (\S+)',line)
        # t is the time
        t = re.findall(date_pattern,line)
        # g is the geolocation
        try:
            g = reader_city.city(z[0])
            g = g.country.iso_code
        except:
            g = 'nonfound'
        com = failed_combo(g,t[0],x[0])
        if z[0] in fail:
            fail[z[0]].append(com)
        else:
            arr = list()
            fail[z[0]] = arr
            fail[z[0]].append(com)

################################################################
import sqlite3

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
        c.execute("INSERT INTO successful_logins VALUES (:hostname,:ip,:date,:geo,:method)",{'hostname':key,'ip':suc.ip,'date':suc.time,'geo':suc.geo,'method':suc.method})


for k,v in success.items():
    for i in range(len(v)):
        insert_success(k,v[i])

conn = sqlite3.connect('invalid.db')

c = conn.cursor()

c.execute("""CREATE TABLE invalid_logins (
    ip text,
    datetime text,
    geolocation text,
    hostname text
)""")

def insert_invalid(k,inc):
    with conn:
        c.execute("INSERT INTO invalid_logins VALUES (:ip,:date,:geo,:hostname)",{'ip':k,'date':inc.time,'geo':inc.geo,'hostname':inc.name})

for k,v in invalid.items():
    for i in range(len(v)):
        insert_invalid(k,v[i])

conn = sqlite3.connect('failed.db')

c = conn.cursor()

c.execute("""CREATE TABLE failed_logins(
    ip text,
    datetime text,
    geolocation text,
    method text
)""")

def insert_invalid(k,fa):
    with conn:
        c.execute("INSERT INTO failed_logins VALUES (:ip,:date,:geo,:method)",{'ip':k,'date':fa.time,'geo':fa.geo,'method':fa.method})

conn.close()