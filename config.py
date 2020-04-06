HUE_ADDRESS = '192.168.0.13'
OMW_KEY = '227ef8a4e315ac8f15ea6a3493f9e318'
OWM_CITY_ID = 5946768
SLEEP_TIME = 50
REFRESH_TIME = 10
#2695
LOW_TEMP = 20
#from weather.py import current_status
import phue
from phue import Bridge
b  = Bridge(HUE_ADDRESS)
#if current_status == 'Clear':

 #   colors = b.set_light(4,'bri',5, transitiontime=1)
#elif current_status == 'Rain':
 #   colors = b.set_light(4, 'bri', 50, transitiontime=1)
#elif current_status == ''
'''
colors = {
    "low_temp" : b.set_light(3,'bri',10),
    "snow" : b.set_light(3,'bri',40),
    "rain" : b.set_light(3,'bri',5),
    "clear": b.set_light(3,'bri',15),
    "clouds" : b.set_light(3,'bri',100),
    "extreme" : b.set_light(3,'bri',200),
}


colors = {
    "low_temp" : [31, 55, 209],
    "snow" : [213, 44, 222],
    "rain" : [44, 222, 65],
    "clouds" : [0, 251, 255],
    "extreme" : [222, 44, 44]
}
'''