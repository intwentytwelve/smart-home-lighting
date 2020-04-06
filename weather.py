#!/usr/bin/env python

import time
import pyowm
from phue import Bridge
#from hue_rgb import Converter

from config import *

owm = pyowm.OWM('da5edc6e45171ba8f35405139b4d3e6e')
#'227ef8a4e315ac8f15ea6a3493f9e318'
current_status = ''
previous_status = ''

b = Bridge('192.168.0.13')
b.connect()

#converter = Converter( )

low_temp = False

color_changed_time = 0

#def changeLightColor(lights, rgb_color):
 #   global color_changed_time
  #  color_changed_time = time.time()
   # for l in lights:
    #    l.xy = converter.rgbToCIE1931(rgb_color[0], rgb_color[1], rgb_color[2])

while True:
    lights = b.lights

    observation = owm.weather_at_id(5946768)
    w = observation.get_weather()

    temp = w.get_temperature('fahrenheit')['temp']
    current_status = w.get_status()

    print ('Temperature:', temp)
    print ('Status:', current_status)

    # Is it time to refresh the color?
    time_to_refresh = time.time() - color_changed_time > REFRESH_TIME

    print ("Time to refresh:", time_to_refresh)
    if b.set_light(1,'on',False):
        b.set_light(1, 'on', True)

    if temp < LOW_TEMP and not low_temp:
        if time_to_refresh:
            print ('Low temperature!')
            low_temp = True
            b.set_light(1, 'bri', 150)
#            changeLightColor(lights, colors["low_temp"])
    elif temp in range(20,30):
        if time_to_refresh:
            print ('Medium temperature!')
            low_temp = True
            b.set_light(1, 'bri', 90)
           # changeLightColor(lights, colors["snow"])
    elif temp in range(30,40):
        if time_to_refresh:
            print ('High temperature!')
            low_temp = True
            b.set_light(1, 'bri', 40)
          #  changeLightColor(lights, colors["rain"])

    elif temp in range(40,50):
        if time_to_refresh:
            print ('Very High temperature!')
            low_temp = True
            b.set_light(1, 'bri', 20)
          #  changeLightColor(lights, b.set_light(1,'bri',10))
    elif temp in range(50,60):
        if time_to_refresh:
            print ('EXTREME!')
            low_temp = True
            b.set_light(3, 'bri', 5)
          #  changeLightColor(lights, colors["extreme"])


    else:
        low_temp = False

    if current_status != previous_status or time_to_refresh:
        print ('Weather changed to:', current_status)

        previous_status = current_status

     #    If there is a defined color for this status: change it
#        if current_status in colors:
 #           changeLightColor(lights, colors[current_status])

    time.sleep(SLEEP_TIME)
