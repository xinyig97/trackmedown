from class_v4 import legit_combo
from class_v4 import invalid_combo
from class_v4 import failed_combo

import output_v4 as ou 
import filter_v4 as f 
import op_v4 as o

import re
from geoip import geolite2
import numpy as np

def handle(fhand):
    date_pattern = re.compile(r'^\S+')
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
                g = geolite2.lookup(z[0])
                g = g.country
            except:
                g = 'nonfound'
            #print(g)
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
                g = geolite2.lookup(z[0])
                g = g.country
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
            #print(line)
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
                g = geolite2.lookup(z[0])
                g = g.country
            except:
                g = 'nonfound'
            #print(g)
            com = failed_combo(g,t[0],x[0],z[0],name[0])
            o.update_failed(com)


#files = ['f27.log','f28.log','f29.log','file.log']
files = ['file.log']
#files = ['f1.log','f2.log','f3.log','f4.log','f5.log','f6.log','f7.log','f8.log','f9.log','f10.log','f11.log','f12.log','f13.log','f14.log','f15.log','f16.log','f17.log','f18.log','f19.log','f20.log','f21.log','f22.log','f23.log','f24.log','f25.log','f26.log','f27.log','f28.log','f29.log']
for i in files:
    fhand = open(i)
    handle(fhand)

ou.output_watchlist()
o.check_first()
# printout to check if work properly 
# print('check success ')
# o.check_succ()
#print('check invalid')
#o.check_in()
#print('check f')
#o.check_f()
# print('check_white')
# o.check_w()
# print('check_watch')
# o.check_wa()



# https://pythonhosted.org/python-geoip/
# https://stackoverflow.com/questions/42616376/install-pandas-on-mac-with-pip/42616942 