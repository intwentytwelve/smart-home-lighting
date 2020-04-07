# Smart home lighting
An adaptive lighting control system that aims to reduce energy consumption while simultaneously preserving the lighting comfort of occupants. Philips Hue light bulbs and Nanoleaf Canvas facilitates interactions and improves data exchange efficiency.

# Table of Contents
1. [Installation](#Installation)
2. [Prerequisites](#Prerequisites)
3. [Roles](#Role)

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
We need to get the IP addresses of Philips Hue and Nanoleaf Canvas to control devices. These can be done by identifying MAC addresses at first. 

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

A library wrote for achieving geofencing function. Geofencing is a location-based service in which an app or other software              uses GPS, RFID, Wi-Fi or cellular data to trigger a pre-programmed action when a mobile device or RFID tag enters or exits a            virtual boundary set up around a geographical location, known as a geofence. Any device that is connecting to the wifi network          makes a broadcast to this port asking for a DHCP address. The DHCP server responds by broadcasting the assigned IP back to that          device as a response over port 67:
```
app.py
```


