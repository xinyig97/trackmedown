import geoip2.database
reader = geoip2.database.Reader('/Users/xinyiguo/Desktop/FA18/python master/geoip_try/geoip/geoip_city/GeoLite2-City.mmdb')
response = reader.city('128.101.101.101')
print(response.country.iso_code)
