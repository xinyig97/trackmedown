# whitelist rule 
# include internal/ external ip addresses belong to ncsa 
# need include partners'
# need to test more on ipv6

import re 
import memorysave as op

external = re.compile(r'141.142.\d{1,3}\W\d{1,3}') #141.142.0.0/16
internal = re.compile(r'172.\b(2[4-9]|3[0-1])\b\W\d{1,3}\W\d{1,3}') #172.24.0.0/13 
third = re.compile(r'198.17.196\W\b(0|0[0-9][0-9]|1[0-2][0-8])\b') #198.17.196.0/25
six = re.compile(r'2620:0:0c80\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]\W[0-9a-e][0-9a-e][0-9a-e][0-9a-e]')
private = re.compile(r'10.\b(0|0[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b\W\b(0|0[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b\W\b(0|0[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b')

def check_for_whitelist(ip):
    if external.match(ip):
     #   op.insert_whitelist(ip)
        return 1
    elif internal.match(ip):
      #  op.insert_whitelist(ip)
        return 1
    elif third.match(ip):
       # op.insert_whitelist(ip)
        return 1
    elif six.match(ip):
        #op.insert_whitelist(ip)
        return 1
    elif private.match(ip):
        #op.insert_whitelist(ip)
        return 1
    else:
        return op.isitin(ip)