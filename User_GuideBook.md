# TrackMeDown User Guideline 
<br/>

#### Purpose for this program 
TrackMeDown analyze login files acquired from system based on login IPs. <br/>
By looking up IPs' geolocation based on MaxMind Geolocation Database (https://github.com/maxmind/GeoIP2-python), it tracks where the user login from. And based on state of the specific login, i.e successful, invalid, or failed, it apply specific filters to detect potential attackers.<br/>

