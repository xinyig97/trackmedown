# TrackMeDown 
general description for this project.
<br/>

## what does TrackMeDown accomplished 
TrackMeDown could successfully parse login files based on states of logins and apply filter with customized rules to categorize suspicious users account, therefore could help system to monitor security condition, protect valuable information, and guard users' account safety. <br/>

## why is TrackMeDown useful 
The easist and most frequent attack happens with attacker trying to breaking into the system with legit user account without users' attention, thus by monitoring login information, we could get a sense of if ths login is from the correct user or might be compromised. <br/>
By alerting on suspicious logins, system managers could make sure of users' accounts safety. <br/>

## what data does TrackMeDown use / create 
- use :
  -system log files provided by user 
  -ip geolocation database from MaxMind (https://github.com/maxmind/GeoIP2-python)
- create :
sqlite databases of the following categories:
  - successful 
  -invalid 
  -failed
  -whitelist
  -watchlist 
 
 ## functionalities TrackMeDown has 
 #### Basic Functions :
 - parse log file based on keyword which indicates the state of logins :
  - 'Accepted' 
  - 'Invalid'
  - 'Failed'
 - analyze the parsed information by collecting username, ip, login time, login method, and login geolocation 
 - categorize corresponding login information into proper database
  - rsuc.db : successful 
  - rinva.db : invalid 
  - rf.db : failed 
 #### Advanced Functions :
 - user can define rules which should be used for analyzing the login information, such as whitelist certain ips, or watchlist certain ips. 
 - user can generate regular report from the information by providing corresponding batch files 
 
 ## reference:
 - GeoIP lookup : (https://github.com/maxmind/GeoIP2-python)
 - SQLite tutorial : 
 (https://www.tutorialspoint.com/sqlite/sqlite_operators.htm) <br/>
 (http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/) <br/>
 (https://docs.python.org/2/library/sqlite3.html) <br/>
 - ip cider notation: (https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#IPv4_CIDR_blocks) <br/> 
 -regex : (https://regexr.com/397dr) </br>
 (https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285) <br/>
 - git: (https://www.atlassian.com/git/tutorials/saving-changes/gitignore) <br/>
 (https://help.github.com/articles/basic-writing-and-formatting-syntax/) <br/> 
 - preliminary rules :(https://answers.uillinois.edu/page.php?id=47572#private) <br/>
 
 ## made by 
 xinyi 
  
 

