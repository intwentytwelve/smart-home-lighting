from phue import Bridge
from pygame import mixer
import time

b = Bridge('192.168.0.13')
b.connect()
b.get_api()

lights = b.lights

# Print light names
for l in lights:
    print(l.name )


#lightningLights = [Keller", "Flurlampe", "Küchenfenster","Femie","Stehlampe", "Tischleuchte"]
lightningLights = ["Haustür","Keller", "Flurlampe", "Küchenfenster","Femie","Stehlampe"]

mixer.init()

def allLightsOn():
    for l in lightningLights:
        b.set_light(1, 'on', True)

def allLightsOff():
    for l in lightningLights:
        b.set_light(1, 'on', False)

def allLightsBrightness(brightness):
    for l in lightningLights:
        b.set_light(1, 'bri', brightness)

def blitz():

    while True:
        allLightsOn()

        allLightsBrightness(250)
        allLightsBrightness(0)
        time.sleep(.7)
        allLightsBrightness(250)
        allLightsBrightness(0)
        time.sleep(.7)
        allLightsBrightness(250)
        allLightsBrightness(0)
        time.sleep(.7)
        allLightsOff()
        time.sleep(1200)

blitz()
