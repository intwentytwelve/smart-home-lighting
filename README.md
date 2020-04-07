# smart-home-lighting
An adaptive lighting control system that aims to reduce energy consumption while simultaneously preserving the lighting comfort of occupants. Philips Hue light bulbs and Nanoleaf Canvas facilitates interactions and improves data exchange efficiency.

# Table of Contents
1. [Installation](#Installation)
2. [Prerequisites](#Prerequisites)
3. [Usage](#Usage)
   * [Methods](#Methods)
   * [Effects](#Effects)
   * [Events](#Events)
   
## Installation
To install the latest stable release:

```bash
pip install kivy
pip install nanoleafapi
pip install phue
pip install requests
pip install json
pip install threading`
pip install pyowm
```

## Prerequisites
We need to get the IP addresses of Philips Hue and Nanoleaf Canvas to control devices. These can be done by identifying MAC addresses at first. 
```bash
from nanoleafapi import Nanoleaf
nl=nanoleaf(ip,auth_token)
```
