# date : 06 - 25 - 2018
# author : xinyi guo
# description : analysize log file from ssh, currently extract out successful login data and keep track of failed ones
# get geo-location of the login based on databse of maxmind : https://dev.maxmind.com/geoip/
# api: https://github.com/maxmind/GeoIP2-python
# output to excel file 
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
date_pattern = re.compile(r'^\S+')
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
        #print(y)
        # z is their ips
        z = re.findall('from (\S+)',line)
        #print(z)
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
            #print(g)
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


# #print("success")
# #print(suc_c)
# for k,v in success.items():
#     #print(k,end='')
#     for i in range(len(v)):
#         #print(' ',end='')
#         #print(v[i].geo)
# #print("invalid")
# #print(in_c)

# for k,v in invalid.items():
#  #   print(k,' ',len(v),' ',end='')
#     for i in range(len(v)):
#         #print(k,' ',len(v),' ',end='')
#         #print(v[i].detail())
# #print("failed")
# #print(f_c)

# for k,v in fail.items():
#  #   print(k,' ',len(v),' ',end='')
#     for i in range(len(v)):
#         #print(k,' ',len(v),' ',end='')
#         #print(v[i].detail())


import pandas as pd

ip = list()
times = list()
time = list()
geo = list()
method = list()

for k,v in fail.items():
    for i in range(len(v)):
        ip.append(k)
        times.append(len(v))
        time.append(v[i].time)
        geo.append(v[i].geo)
        method.append(v[i].method)
        
df = pd.DataFrame({'ip':ip,
                  'times':times,
                  'datetime':time,
                  'geo':geo,
                  'method':method})

writer = pd.ExcelWriter("fail_list.xlsx",
                        engine = 'xlsxwriter',
                        )

df.to_excel(writer,sheet_name='Sheet1')
workbook=writer.book
worksheet = writer.sheets['Sheet1']
writer.save()

sname = list()
sip = list()
stimes = list()
stime = list()
sgeo = list()
smethod = list()

for k,v in success.items():
    for i in range(len(v)):
        sname.append(k)
        sip.append(v[i].ip)
        stimes.append(len(v))
        stime.append(v[i].time)
        sgeo.append(v[i].geo)
        smethod.append(v[i].method)
        
df = pd.DataFrame({'name':sname,
                   'ip':sip,
                  'times':stimes,
                  'datetime':stime,
                  'geo':sgeo,
                  'method':smethod})

writer = pd.ExcelWriter("success.xlsx",
                        engine = 'xlsxwriter',
                        )

df.to_excel(writer,sheet_name='Sheet1')
workbook=writer.book
worksheet = writer.sheets['Sheet1']
writer.save()

iip = list()
itimes = list()
itime = list()
igeo = list()
iname= list()

for k,v in invalid.items():
    for i in range(len(v)):
        iip.append(k)
        itimes.append(len(v))
        itime.append(v[i].time)
        igeo.append(v[i].geo)
        iname.append(v[i].name)
        
df = pd.DataFrame({'ip':iip,
                  'times':itimes,
                  'datetime':itime,
                  'geo':igeo,
                  'name':iname})

writer = pd.ExcelWriter("invalid.xlsx",
                        engine = 'xlsxwriter',
                        )

df.to_excel(writer,sheet_name='Sheet1')
workbook=writer.book
worksheet = writer.sheets['Sheet1']
writer.save()

