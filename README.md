# Smart home lighting
An adaptive lighting control system that aims to reduce energy consumption while simultaneously preserving the lighting comfort of occupants. Philips Hue light bulbs and Nanoleaf Canvas facilitates interactions and improves data exchange efficiency.

# Table of Contents
1. [Installation](#Installation)
2. [Prerequisites](#Prerequisites)
3. [Roles](#Roles)

## Installation
To install the latest stable release of libraries used:

```bash
pip install kivy           #Open source framework based on Python, providing GUI for developing software
pip install nanoleafapi    #nanoleafapi is a Python 3 wrapper for the Nanoleaf OpenAPI
pip install phue           #Full featured Python library to control the Philips Hue lighting system
pip install requests       #The requests library is a standard for making HTTP requests in Python
pip install json           #It can also convert Python dictionaries or lists into JSON strings
pip install threading      #Non blocking timer for dynamic control
pip install pyowm          #PyOWM is a client Python wrapper library for accessing OpenWeatherMap web APIs
```

## Prerequisites
Users need to get the IP addresses of Philips Hue and Nanoleaf Canvas to control devices. These can be done by identifying MAC addresses at first. 

This is for connecting Nanoleaf Canvas:
```bash
from nanoleafapi import Nanoleaf
nl=nanoleaf(ip,auth_token)
```
This is for connecting Philips Hue:
```bash
from phue import Bridge
b=Bridge(ip)
```

## Roles

A library to achieve geofencing function for Philips Hue. Geofencing is a location-based service in which an app or other software uses GPS,  RFID, Wi-Fi or cellular data to trigger a pre-programmed action when a mobile device or RFID tag enters or exits a virtual boundary set up around a geographical location, known as a geofence. Any device that is connecting to the wifi network makes a broadcast to this port asking for a DHCP address. The DHCP server responds by broadcasting the assigned IP back to that device as a response over port 67:
```
app.py
```

It is the background picture of mobile application:
```
background.jpg
```

The framework of application. Kv language is used for describing user interfaces and adding widgets to GUI and widgets are provided with functionalities to achieve the control of motion events. The functionalities of Nanoleaf Canvas are manual control, sunset/sunrise, weather reaction, temperature reaction and notification respectively:
```
main.py
```

The Android .apk file of adaptive control lighting system:
```
myapp__armeabi-v7a-0.1-armeabi-v7a-debug.apk
```

Notification by flashing of Nanoleaf Canvas. It imitates a process that server sends a message through IFTTT, then users get a notification on mobile phone. Nanoleaf Canvas detects the notificaiton and flashes to notify users there is a message:
```
notice.py
```

Music feature is allowing Phillips Hue light bulbs to react to the beats and sync the lights flash to the background music. Fast Fourier transforms are widely used for applications in engineering, music, science, and mathematics. Accordingly this function is used to determine the brightness of the lamps concerning an activation threshold that constantly checks the brightness of the lamps:
```
rhythm.py
```

Reducing the screen time is one of the most important factors that requires significant attention since it affects the users personal
wellbeing. Hence, this research propounds a more visualized manner for Philips Hue lab and bed room bulbs to remind the users to rest their eyes after staring at the computer for a long period of time:
```
screen.py
```

This features aims to make the hue light bulbs work with respect to weather condition. In this regard, this research has used Open Weather Maps as the weather API to get the current weather conditions for one place and then changes the color of the brightness of the Hue lamps accordingly:
```
weather.py
```
