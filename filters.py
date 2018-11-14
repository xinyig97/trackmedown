# whitelist rule 
# include internal/ external ip addresses belong to ncsa 
# need include partners'
# need to test more on ipv6


import re 

external = re.compile(r'141.142.\d{1,3}\W\d{1,3}') #141.142.0.0/16
internal = re.compile(r'172.\b(2[4-9]|3[0-1])\b\W\d{1,3}\W\d{1,3}') #172.24.0.0/13 
third = re.compile(r'198.17.196\W\b(0|0[0-9][0-9]|1[0-2][0-8])\b') #198.17.196.0/25
six = re.compile(r'2620:0:0c80\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]')

def check_for_whitelist(a,ip):
    a = 0
    if external.match(ip):
        a = 1
        return 
    elif internal.match(ip):
        a = 1
        return 
    elif third.match(ip):
        a = 1
        return 
    elif six.match(ip):
        a = 1
        return 
    else:
        a = 0
        return 
