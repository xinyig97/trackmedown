# trackmedown

- for project details, check out General.md 
- for funtionality and guidelines, checkout User_Guide.md 
- for debugged version, check out Final Version 
- for dev history, check out : preliminary , Version 1, Version 2 

## to do 
- [ ] try immigrate from sqlite3 db into postgres
- [ ] generate alert system on a regular base - December 
- [x] whitelist and watchlist rule 
- [ ] more data to test 

### resources :
- Batch files : (http://gobruen.com/progs/dos_batch/dos_batch.html)

## dev log 
### dev log 10-31:
initialize_db.py - create corresponding list at beginning, run once ONLY <br/>
whitelist.py - update whitelist with ips that are from internal or been authenticated already, no need to keep alert on  <br/>
watchlist.py - update watchlist with ips that are suspicious and need to be alerted immediately / in a timely manner <br/>
v2.py - slightly modification with arrangement of codes and functions <br/>

### dev log 11-07:
classes.py - classes definition, accessed by other functions in py <br/>
operations.py - functions used to interact with database (query and insert) <br/>
operations.py replaced whitelist.py and watchlist.py <br/>
v2.py - directly interaction with databases <br/>

### dev log 11-14: 
v2.py : plcae appropriate filters for whitelist rule  <br/>
filters.py : using regex for selecting ips <br/>

### dev log 11-28:
validated output <br/>
fixed bugs <br/>

### dev log 11-29:
add functionalities that 
 - you can manually whitelisted ip 
 - you can remove entry from watchlist once you get the confimation and choose if reset the count <br/>
 
add output the watchlist result into excel file named 'files.xlsx' <br/>

### dev log 11-30:
tested on new data and fixed bugs 

### dev log 12-05:
added very first spotted login based on ip and hostname, thus for later reference <br/>
update interaction with the databases , organizes them in a more concise way 
 - manually add whitelist entry 
 - remove entry from watchlist and reset the count 
 - observe an entry from it's very first appearance and most recent appearance 
 
 ### dev log 12-07:
 tried depopulating whitelist database memory by directly comparing with filter for running time efficieny, which is version 4<br/>
 sub maxmind database download with geoip module <br/>

## bug log :
#### 11-07 : calling functions / classes defined in a different file in python 3 :
(https://stackoverflow.com/questions/31540009/importerror-cannot-import-name-in-python/31540162 )
#### 11-30: keyword specification 
'Failed' 'Invalid' 'Accepted' are currently keyword to find information when parsing through log file, however, there may be other cases where also contain those keywords. <br/>
 - could solve by testing more data 
 - or by identifying all possible cases that could contain those keywords but irrelevant to our purposes
 #### 12-05: python use copying variable when calling functions

