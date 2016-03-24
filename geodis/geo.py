import redis
import geodis

from geodis import city

'''
See docs here:
https://github.com/EverythingMe/geodis

Use this command if redis database is not already populated (on windows):

python env\Lib\site-packages\geodis\geodis -z -f env\Lib\site-packages\geodis\data\zipcode.csv run

remember to change port as needed
'''


conn = redis.Redis(host='127.0.0.1', port='6379')

print city.City.getByLatLon(31.78,35.21, conn)
