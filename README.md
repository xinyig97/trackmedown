# trackmedown
geoip monitor <br/>
check log file, distinguish valid, invalid, failed login attempts <br/>
output three excels with each content correspondingly <br/>

reference: <br/>
geoip lookup api from maxmind :
https://github.com/maxmind/GeoIP2-python  <br/>
sqlite tutorial :
https://www.tutorialspoint.com/sqlite/sqlite_operators.htm <br/>
http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/ <br/>
https://docs.python.org/2/library/sqlite3.html <br/>

File Description: <br/>
progj.py : version 1 of geolocation monitor with output in excel local doc  <br/>
v2.py : version 2 with output as python sqlite3 db files <br/>
initialize_db.py : run once ONLY at the beginning to create corresponding databases <br/>
[NOT USED] whitelist.py : update whitelist with ips that are from internal or been authenticated already, no need to keep alert on  <br/>
[NOT USED] watchlist.py : update watchlist with ips that are suspicious and need to be alerted immediately / in a timely manner <br/>
classes.py : classes definition <br/>
operations.py : functions used to interact with database <br/>

TODO: <br/>
try immigrate from sqlite3 db into postgres - might need more time on this one - November <br/>
generate email alerting system with a regular base  - November <br/>
watchlist rule && whitelist rule needed - November <br/>


dev log 10-31:<br/>
initialize_db.py - create corresponding list at beginning, run once ONLY <br/>
whitelist.py - update whitelist with ips that are from internal or been authenticated already, no need to keep alert on  <br/>
watchlist.py - update watchlist with ips that are suspicious and need to be alerted immediately / in a timely manner <br/>
v2.py - slightly modification with arrangement of codes and functions <br/>

dev log 11-07:<br/>
classes.py - classes definition, accessed by other functions in py <br/>
operations.py - functions used to interact with database (query and insert) <br/>
operations.py replaced whitelist.py and watchlist.py <br/>
v2.py - directly interaction with databases <br/>

bug log :<br>
11-07 : calling functions / classes defined in a different file in python 3 : <br/> https://stackoverflow.com/questions/31540009/importerror-cannot-import-name-in-python/31540162 
