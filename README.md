# trackmedown
geoip monitor <br/>
check log file, distinguish valid, invalid, failed login attempts <br/>
output three excels with each content correspondingly <br/>

reference: <br/>
geoip lookup api from maxmind :
https://github.com/maxmind/GeoIP2-python

<p1>File Description</p1>
progj.py : version 1 of geolocation monitor with output in excel local doc 
v2.py : version 2 with output as python sqlite3 db files
initialize_db.py : run once ONLY at the beginning to create corresponding databases 
whitelist.py : functions that to upate whitelisted- ips, and query from it 
watchlist.py : funtions that to update watchlisted-ips and query from it


TODO: 
try immigrate from sqlite3 db into postgres - might need more time on this one 


dev log 10-31:<br/>
initialize_db.py - create corresponding list at beginning, run once ONLY
whitelist.py - update whitelist with ips that are from internal or been authenticated already, no need to keep alert on 
watchlist.py - update watchlist with ips that are suspicious and need to be alerted immediately / in a timely manner 
v2.py - slightly modification with arrangement of codes and functions 
