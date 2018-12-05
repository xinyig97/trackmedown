# User Guides for TrackMeDown 
including explaination of fucntions and how to use this program on locals 

## Funtions and Files explaination 
files interface for TrackMeDown 

### Version 1 
- progj.py : the first version with parsing output in excels 

### Version 2 
- v2.py : the second version with usage of database but with functions all around 
- classes.py : classes definition 
- filters.py : rules definition 
- initialize_db.py : database initialization 
- operations.py : interaction between program and database, including insert, search for success, invalid, and failed databases 
- watchlist.py : interaction between program and watchlist database 
- whitelist.py : interaction between program and whitelist database 

### Final Version 
- version3.py : integrated functions, cleaned up interfaces, more concisely 
- class_v3.py : classes definition 
- filters.py : rules definition 
- ini_v3.py : database initialization 
- op_v3.py : interaction between program with all databases 
- addwhitelist.py : manually insert whitelisted ip to the database 
- output.py : generate excel output from watchlist database to excel readable by humans 
- notwatching.py : manually delete entry from watchlist 
- actions.py : manually checkout one entry's first login appearance and its most recent login appearance 
- interaction.py : combined user interaction with databases 

### orig. file
log files used for testing, could not posted 

### preliminary 
- try.py : first time parsing logfile with information saved in dictionary and no output 

## how to use 
- make sure you have python3 installed with pandas module 
- download MaxMind database : (https://dev.maxmind.com/geoip/geoip2/geolite2/)
- find the path to your database on your local PC 
  - navigate to the your database by using cd on terminal 
  - print out path by using pwd 
  - copy the path and paste into /Final Verision/version3.py line 13 
- get your log file and convert into .log format, put it in /Final Version/version3.py line 14 
  - if your file is in .gz.Z , run ''' gzcat *.gz > file.log''' 
- run /Final Version/ini_v3.py first 
- run /Final Version/version3.py and your resulted database should exist in your local folder, the resulted output of watchlist is in files.xlsx 
- to access data within each database, comment out line 94-103 in /Final Version/version3.py 

### user interaction with database:

run 'python interaction.py' and follow the prompt 

- to manually whitelist ip
- to manually delete entry from watchlist 
  - notice: deletion is an one-time action and not revertable, be careful for that
- to checkout one entry's peorid of existing 

### to change whitelist rule / watchlist rule 
- whitelist : change should be made in /Final Version/filters.py 
- watchlist : 
 - current threshold is 5, value change should be made in /Final Version/op_v3.py line 110 for 'invalid' and line 168 for 'failed'
 - if need more complicated rules, please add another .py files 


