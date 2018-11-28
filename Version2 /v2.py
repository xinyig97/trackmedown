# date : 11 - 14 - 2018
# author : xinyi guo
# UPDATE : place appropriate filter for whitelist rule 
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
    
# gonna use regex to grab info
from classes import legit_combo
from classes import invalid_combo
from classes import failed_combo
import re
import geoip2.database
import numpy as np
from watchlist import insert_watched,search_in_watchedl
from whitelist import insert_whitelist,search_in_whitel
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


import filters as f 
import operations as o
# for successful logins, record on the success table 
# add internal to whitelist (for now, maybe more reuqirement later on)
for k,v in success.items():
    for i in range(len(v)):
        o.insert_success(k,v[i])
        a = 0
        f.check_for_whitelist(a,v[i].ip)
        if a ==1 :
            o.insert_whitelist(k,v[i])

# for invalid logins, record on invalid table 
# check if they exist in whitelist, if so, ignore 
for k,v in invalid.items():
    for i in range(len(v)):
        o.search_in_whitel(v[i].name,k,a)
        if a == 0:
            o.insert_invalid(k,v[i])
        #do something with the watch list, need requirements in terms of that 
        

# for failed logins, record on invalid table 
for k,v in fail.items():
    for i in range(len(v)):
        o.insert_failed(k,v[i])
        o.insert_watchlist_f(k,k)



