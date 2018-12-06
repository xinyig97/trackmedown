from class_v3 import legit_combo
from class_v3 import invalid_combo
from class_v3 import failed_combo
import output as ou 
import filters as f 
import op_v3 as o

import re
import geoip2.database
import numpy as np

def handle(fhand):
    for line in fhand:
        # successful users
        if ' Accepted ' in line:
            print(line)
            # x is the method they loggin in
            x = re.findall('Accepted (\S+)',line)
            #print(x)
            # y is their username
            y = re.findall('for (\S+)',line)
            #print(y)
            #z is their ips
            z = re.findall('from (\S+)',line)
            #print(z)
            # t is the time
            t = re.findall(date_pattern,line)
            #print(t)
            # g is the geolocation
            try:
                g = reader_city.city(z[0])
                g = g.country.iso_code
            except:
                g = 'nonfound'
            com = legit_combo(z[0],g,t[0],x[0],y[0])
            o.update_success(com)
        elif 'Invalid' in line:
            if('Invalid argument' in line):
                break
            #print(line)
            # y is their username
            y = re.findall('user (\S+)',line)
            if len(y) == 0:
                y = 'nonfound'
            #print(y)
            # z is their ips
            z = re.findall('from (\S+)',line)
            #print(z[0])
            # t is the time
            t = re.findall(date_pattern,line)
            #print(t)
            # g is the geolocation
            try:
                g = reader_city.city(z[0])
                g = g.country.iso_code
                #print(g.country.iso_code)
            except:
                g = 'nonfound'
            #print(g)
            com = invalid_combo(y[0],g,t[0],z[0])
            o.update_invalid(com)
        elif 'Failed' in line:
            if('Failed to apply' in line):
                break
            if('Failed to release session' in line):
                break
            print(line)
            if('Failed to' in line):
                break
        #    x is the method they loggin in
            x = re.findall('Failed (\S+)',line)
            #print(x[0])
            # z is their ips
            z = re.findall('from (\S+)',line)
            #print(z[0])
            # t is the time
            t = re.findall(date_pattern,line)
            #print(t[0])
            # name is the user namae 
            name = re.findall('(?<= for invalid user )(.*)(?= from )',line)
            if not name:
                name = re.findall('(?<= for )(.*)(?= from )',line)
            #print(name)
            #name = ['0']
            # g is the geolocation
            try:
                g = reader_city.city(z[0])
                g = g.country.iso_code
            except:
                g = 'nonfound'
            #print(g)
            com = failed_combo(g,t[0],x[0],z[0],name[0])
            o.update_failed(com)


#local path to geolite2-city.mmdb database 
files = ['f27.log','f28.log','f29.log','file.log']
#files = ['f7.log']
#files = ['f7.log','f8.log','f9.log','f10.log','f11.log','f12.log','f13.log','file.log']
reader_city = geoip2.database.Reader('/Users/xinyiguo/Desktop/clean/ransome/python master/geoip_try/geoip/geoip_city/GeoLite2-City.mmdb')
date_pattern = re.compile(r'^\S+')
suc_c = 0
in_c = 0
f_c=0
for i in files:
    fhand = open(i)
    handle(fhand)

ou.output_watchlist()
o.check_first()
# printout to check if work properly 
#print('check success ')
#o.check_succ()
#print('check invalid')
#o.check_in()
#print('check f')
#o.check_f()
# print('check_white')
# o.check_w()
# print('check_watch')
# o.check_wa()
