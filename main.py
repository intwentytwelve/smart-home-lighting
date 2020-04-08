
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.image import Image
from kivy.uix.switch import Switch
from nanoleafapi import Nanoleaf
from kivy.graphics import *
from phue import Bridge
from nanoleafapi import RED, ORANGE, YELLOW, BLUE, GREEN, WHITE, LIGHT_BLUE, PINK, PURPLE
import requests
import json
from threading import Timer
import datetime
from kivy.uix.screenmanager import Screen, ScreenManager
import pyowm
import random
from kivy.lang import Builder
import time
from kivy.uix.checkbox import CheckBox


kv = """
WindowManager:
    MainWindow:
    SecondWindow:
    ThirdWindow:
<MainWindow>:
    name:'main'
    RootWidget:  # covers the entire window             
        canvas:
            Rectangle:
                source: 'background.jpg'  
                pos: self.pos
                size: self.size
        BoxLayout:
            orientation: 'vertical'
            Label:
                size_hint_y: .1
                text: 'Nanoleaf'
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                padding: dp(10), dp(10)

            GridLayout:
                cols: 6
                rows: 3
                spacing: dp(10)
                padding: dp(10)
                Button:
                    text: 'Connect'
                    on_release:app.connect_nanoleaf()
                    on_press:on.disabled=False
                    on_press:off.disabled=False
                    on_press:color.disabled=False
                    on_press:flash.disabled=False
                    on_press:random.disabled=False
                    on_press:weather.disabled=False
                    on_press:temp.disabled=False
                    on_press:hue_slider.disabled=False
                    on_press:brightness_slider.disabled=False
                    on_press:sun.disabled=False


                Button:
                    id:on
                    text: 'On'
                    disabled:True
                    on_release:app.power_on()
                Button:
                    id:off
                    text: 'Off'
                    disabled:True
                    on_release:app.power_off()
                Button:
                    id:color
                    text: 'Color'
                    disabled:True
                    on_release:app.set_color()
                Button:
                    id:flash
                    text: 'Flash'
                    disabled:True
                    on_release:app.flash()
                Button:
                    id:random
                    text: 'Random'
                    disabled:True
                    on_release:app.random_color()
                Label:
                    text: 'Hue'
                Slider:
                    id: hue_slider
                    min:0
                    max:100
                    disabled:True
                    on_value:app.on_value1(int(hue_slider.value))
                Label
                    text: str(int(hue_slider.value))
                Label:
                    text: 'Brightness'
                Slider:
                    id: brightness_slider
                    min:0
                    max:100
                    disabled:True
                    on_value:app.on_value2(int(brightness_slider.value))
                Label:

                    text: str(int(brightness_slider.value))
                Label:
                    text:'Weather'
                Label:
                    text:''
                Label:
                    text:'Temperature'
                Label:
                    text:''
                Label:
                    text:'Sun'
            GridLayout:
                size_hint_y: .3
                cols:3
                rows:1

                Switch:
                    id:weather
                    disabled:True
                    on_active:app.activeValue1(self.active)
                    


                Switch:
                    id:temp
                    disabled:True
                    on_active:app.activeValue2(self.active)


                Switch:
                    id:sun
                    disabled:True
                    on_active:app.activeValue3(self.active)





            Label:
                size_hint_y: .1
                text: 'Philips Hue'
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                padding: dp(10), dp(10)

            BoxLayout:
                orientation: 'horizontal'
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    size_hint_x: .25
                    Label:
                    Button:  # This is a place holder that centers the button
                        size_hint_y: None
                        #height: grid_button.height
                        text: 'Connect'
                        on_release:app.connect_hue()
                        on_press:on1.disabled=False
                        on_press:off1.disabled=False

                        on_press:lab.disabled=False
                        on_press:on2.disabled=False
                        on_press:off2.disabled=False

                        on_press:bed.disabled=False
                        on_press:on3.disabled=False
                        on_press:off3.disabled=False

                        on_press:living.disabled=False
                        on_press:on4.disabled=False
                        on_press:off4.disabled=False

                        on_press:white_slider.disabled=False

                    Button:
                        text:'Next'
                        on_release:
                            app.root.current='second'
                            root.manager.transition.direction='left'

                GridLayout:
                    cols: 5
                    rows: 4
                    spacing: dp(10)
                    padding: dp(10)
                    Button:
                        id:on1
                        text:'On'
                        disabled:True
                        on_release:app.lab_on()

                    Button:
                        id:off1
                        text:'Off'
                        disabled:True
                        on_release:app.lab_off()


                    Label:
                        text: 'Lab'   
                    Slider:
                        id: lab
                        min:0
                        max:255
                        disabled:True
                        on_value:app.on_value3(int(lab.value))
                    Label:
                        text: str(int(lab.value))

                    Button:
                        id:on2
                        text:'On'
                        disabled:True
                        on_release:app.bed_on()
                    Button:
                        id:off2
                        text:'Off'
                        disabled:True
                        on_release:app.bed_off()

                    Label:
                        text: 'Bed'
                    Slider:
                        id: bed
                        min:0
                        max:255
                        disabled:True
                        on_value:app.on_value4(int(bed.value))
                    Label:
                        text: str(int(bed.value))

                    Button:
                        id:on3
                        text: 'On'
                        disabled:True
                        on_release:app.living_on()
                    Button:
                        id:off3
                        text: 'Off'
                        disabled:True
                        on_release:app.living_off()


                    Label:
                        text: 'Living'
                    Slider:
                        id: living
                        min:0
                        max:255
                        disabled:True
                        on_value:app.on_value5(int(living.value))
                    Label:
                        text: str(int(living.value))

                    Button:
                        id:on4
                        text: 'On'
                        disabled:True
                        on_release:app.white_on()
                    Button:
                        id:off4
                        text: 'Off'
                        disabled:True
                        on_release:app.white_off()

                    Label:
                        text: 'White'
                    Slider:
                        id: white_slider
                        min:0
                        max:255
                        disabled:True
                        on_value:app.on_value6(int(white.value))
                    Label:
                        text: str(int(white_slider.value))
<SecondWindow>:
    name:'second'
    RootWidget:  # covers the entire window             
        canvas:
            Rectangle:
                source: 'background.jpg'  
                pos: self.pos
                size: self.size
        Label:
            size_hint_y: .1
            #text: 'philips hue'
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            padding: dp(10), dp(10)

        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation: 'vertical'
                padding: dp(10)
                size_hint_x: .25
                Button:
                    text:'Back'
                    on_release:
                        app.root.current='main'
                        root.manager.transition.direction='right'
                Button:
                    text:'Connect'
                    on_release:app.connect_hue()
                    
                Button:
                    text:'Next'
                    on_release:
                        app.root.current='third'
                        root.manager.transition.direction='left'

            GridLayout:
                cols: 2
                rows: 12
                spacing: dp(10)
                padding: dp(10)

                Label:
                    text:'Labs Sunet/Sunrise'
                Switch:
                    id:sun1
                    #disabled:True
                    on_active:app.activeValue4(self.active)
                Label:
                    text:'Labs Weather'
                Switch:
                    id:sun5
                    #disabled:True
                    on_active:app.activeValue8(self.active)
                Label:
                    text:'Lab Geofencing'
                Switch:
                    id:sun9
                    #disabled:True
                    on_active:app.activeValue12(self.active)
                    
                Label:
                    text:'Beds Sunet/Sunrise'
                    
                Switch:
                    id:sun2
                    #disabled:True
                    on_active:app.activeValue5(self.active)
                Label:
                    text:'Beds Weather'
                    
                Switch:
                    id:sun6
                    #disabled:True
                    on_active:app.activeValue9(self.active)
                
                Label:
                    text:'Bed Geofencing'
                Switch:
                    id:sun10
                    #disabled:True
                    on_active:app.activeValue13(self.active)
                
                Label:
                    text:'Livings Sunet/Sunrise'
                Switch:
                    id:sun3
                    #disabled:True
                    on_active:app.activeValue6(self.active)
                Label:
                    text:'Livings Weather'
                    
                Switch:
                    id:sun7
                    #disabled:True
                    on_active:app.activeValue10(self.active)
                
                Label:
                    text:'Livings Gwofencing'
                Switch:
                    id:sun11
                    #disabled:True
                    on_active:app.activeValue14(self.active)
                    
                Label:
                    text:'Whites Sunet/Sunrise'
                Switch:
                    id:sun4
                    #disabled:True
                    on_active:app.activeValue7(self.active)
                Label:
                    text:'Whites Weather'
                    
                Switch:
                    id:sun8
                    #disabled:True
                    on_active:app.activeValue11(self.active)
                Label:
                    text:'Whites Geofencing'
                Switch:
                    id:sun12
                    #disabled:True
                    on_active:app.activeValue15(self.active)
                    
                    
                    
<ThirdWindow>:                    
                
    name:'third'
    RootWidget:  # covers the entire window             
        canvas:
            Rectangle:
                source: 'background.jpg'  
                pos: self.pos
                size: self.size
        Label:
            size_hint_y: .1
            #text: 'philips hue'
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            padding: dp(10), dp(10)

        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation: 'vertical'
                padding: dp(10)
                size_hint_x: .25
                Button:
                    text:'Back'
                    on_release:
                        app.root.current='second'
                        root.manager.transition.direction='right'
                Button:
                    text:'Connect'
                    on_release:app.connect_hue()
                    

            GridLayout:
                cols: 2
                rows: 8
                spacing: dp(10)
                padding: dp(10)

                Label:
                    text:'Labs Music Flash'
                Label:
                    text:'Labs Screen Time'
                  
                Switch:
                    id:sun1
                    #disabled:True
                    on_active:app.activeValue16(self.active)               
                
                
                Switch:
                    id:sun2
                    #disabled:True
                    on_active:app.activeValue17(self.active) 

                Label:
                    text:'Beds Music Time'
                Label:
                    text:'Beds Screen Time'    
                
                Switch:
                    id:sun3
                    #disabled:True
                    on_active:app.activeValue18(self.active)               
                
                
                Switch:
                    id:sun4
                    #disabled:True
                    on_active:app.activeValue19(self.active)   
                Label:
                    text:'Livings Music Flash'    
                Label:
                    text:'Livings Screen Time'
                
                Switch:
                    id:sun5
                    #disabled:True
                    on_active:app.activeValue20(self.active)               
                
                
                Switch:
                    id:sun6
                    #disabled:True
                    on_active:app.activeValue21(self.active)
                    
                Label:
                    text:'Whites Music Flash'   
                Label:
                    text:'Whites Screen Time'
                Switch:
                    id:sun7
                    #disabled:True
                    on_active:app.activeValue22(self.active)               
                
                
                Switch:
                    id:sun8
                    #disabled:True
                    on_active:app.activeValue23(self.active)  
                    
                
                    
                    



"""


class RootWidget(FloatLayout):
    pass


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class TestApp(App):

    def connect_nanoleaf(self, *args):
        try:
            self.nl = Nanoleaf('192.168.0.108')
            auth_token = 'authentication token' #Real token was removed by authors for protecting security
            self.nl = Nanoleaf('192.168.0.108', auth_token)
        except Exception:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='No valid nanoleaf device found'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def power_on(self, *args):
        try:
            self.nl.power_on()
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def power_off(self, *args):
        try:
            self.nl.power_off()
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def turn_up(self, *args):
        try:
            if self.nl.get_power() == True:
                self.nl.increment_brightness(10)
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def turn_down(self, *args):
        try:
            if self.nl.get_power() == True:
                if self.nl.get_brightness() > 0:
                    self.nl.set_brightness(self.nl.get_brightness() - 10)
                else:
                    self.nl.set_brightness(0)
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def set_color(self, *args):
        try:
            if self.nl.get_power() == True:
                content = GridLayout(cols=2)
                content_admit = Button(text='OK')
                content_cancel = Button(text='Cancel')
                self.content_input = TextInput(multiline=False)
                content.add_widget(Label(text='Please input color in R,G,B:'))
                content.add_widget(self.content_input)
                content.add_widget(content_admit)
                content.add_widget(content_cancel)
                popup = Popup(title='Message', content=content, auto_dismiss=False)
                content_cancel.bind(on_release=popup.dismiss)
                content_admit.bind(on_release=self.pressed)
                popup.open()
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def pressed(self, instance):
        color = self.content_input.text
        try:
            if color=='RED':
                self.nl.set_color(RED)
            elif color=='ORANGE':
                self.nl.set_color(ORANGE)
            elif color=='YELLOW':
                self.nl.set_color(YELLOW)
            elif color=='BLUE':
                self.nl.set_color(BLUE)
            elif color=='GREEN':
                self.nl.set_color(GREEN)
            elif color=='WHITE':
                self.nl.set_color(WHITE)
            elif color=='LIGHT_BLUE':
                self.nl.set_color(LIGHT_BLUE)
            elif color=='PINK':
                self.nl.set_color(PINK)
            elif color=='PURPLE':
                self.nl.set_color(PURPLE)
            elif type(int(color.split(',')[0])) == int and type(int(color.split(',')[1])) == int and type(
                    int(color.split(',')[2])) == int and color.count(',') == 2 and \
                    (0 <= int(color.split(',')[0]) <= 255) == True and (
                    0 <= int(color.split(',')[1]) <= 255) == True and (0 <= int(color.split(',')[2]) <= 255) == True:
                self.nl.set_color((int(color.split(',')[0]), int(color.split(',')[1]), int(color.split(',')[2])))
        
                
        except ValueError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please input valid numbers'))
            content_cancel = Button(text='OK')
            content.add_widget(content_cancel)
            popup = Popup(title='Warning', content=content, auto_dismiss=False)
            content_cancel.bind(on_release=popup.dismiss)
            popup.open()
        except IndexError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please input valid numbers'))
            content_cancel = Button(text='OK')
            content.add_widget(content_cancel)
            popup = Popup(title='Warning', content=content, auto_dismiss=False)
            content_cancel.bind(on_release=popup.dismiss)
            popup.open()

    def flash(self, *args):
        try:
            self.nl.identify()
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def random_color(self, *args):
        try:
            if self.nl.get_power() == True:
                R = random.randint(0, 255)
                G = random.randint(0, 255)
                B = random.randint(0, 255)
                self.nl.set_color((R, G, B))
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def on_value2(self, brightness):
        try:
            self.brightnessValue = "%d" % brightness
            self.nl.set_brightness(int(self.brightnessValue))
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def on_value1(self, hue):
        try:
            self.hueValue = "%d" % hue
            self.nl.set_hue(int(self.hueValue))
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def weatherControl(self):
        # self.state=active
        try:
            if self.aV1 == True and self.nl.get_power() == True:
                url = 'http://api.openweathermap.org/data/2.5/weather?id=5946768&appid=authentication token'#Real token was removed by authors for protecting security
                json_data = requests.get(url).json()
                condition = json_data['weather'][0]['main']
                '''content=GridLayout(cols=1)
                content_admit=Button(text='OK')
                content.add_widget(Label(text='Weather is: '+condition))
                content.add_widget(content_admit)
                popup = Popup(title='Message',content=content,auto_dismiss=False)
                content_admit.bind(on_release=popup.dismiss)
                popup.open()'''
                if (condition == "Clear"):
                    self.sunny()
                elif (condition == "Clouds"):
                    self.cloudy()
                elif (condition == "Snow"):
                    self.snowy()
                elif (condition == "Rain"):
                    self.rainy()
                else:
                    pass
                t = Timer(5, self.weatherControl)
                t.start()
            else:
                t = Timer(5, self.weatherControl)
                t.cancel()

        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def sunControl(self):
        try:
            if self.aV3 == True:
                t1 = datetime.datetime.now()
                if t1.hour >= 8 and t1.hour <= 16:
                    self.nl.power_off()

                elif t1.hour == 7:
                    if t1.minute >= 40:
                        self.nl.power_off()
                    else:
                        self.nl.power_on()

                elif t1.hour == 17:
                    if t1.minute <= 45:
                        self.nl.power_off()
                    else:
                        self.nl.power_on()

                else:
                    self.nl.power_on()
                t = Timer(5, self.sunControl)
                t.start()

            else:
                # self.nl.power_off()
                t = Timer(5, self.sunControl)
                t.cancel()

        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def activeValue1(self, active):
        self.aV1 = active
        self.weatherControl()

    def activeValue2(self, active):
        self.aV2 = active
        self.tempControl()

    def activeValue3(self, active):
        self.aV3 = active
        self.sunControl()

    def activeValue4(self, active):
        self.aV4 = active
        self.sunLab()

    def activeValue5(self, active):
        self.aV5 = active
        self.sunBed()

    def activeValue6(self, active):
        self.aV6 = active
        self.sunLiving()

    def activeValue7(self, active):
        self.aV7 = active
        self.sunWhite()

    def activeValue8(self, active):
        self.aV8 = active
        self.weatherLab()

    def activeValue9(self, active):
        self.aV9 = active
        self.weatherBed()

    def activeValue10(self, active):
        self.aV10 = active
        self.weatherLiving()

    def activeValue11(self, active):
        self.aV11 = active
        self.weatherWhite()

    def activeValue12(self, active):
        self.aV12 = active
        self.geofencinglab()

    def activeValue13(self, active):
        self.aV13 = active
        self.geofencingBed()

    def activeValue14(self, active):
        self.aV14 = active
        self.geofencingLiving()

    def activeValue15(self, active):
        self.aV15 = active
        self.geofencingWhite()



    def activeValue16(self, active):
        self.aV16 = active
        self.musiclab()

    def activeValue17(self, active):
        self.aV17 = active
        self.labscreen()





    def activeValue18(self, active):
        self.aV18 = active
        self.musicbed()

    def activeValue19(self, active):
        self.aV19 = active
        self.bedscreen()


    def activeValue20(self, active):
        self.aV20 = active
        self.musicliving()


    def activeValue22(self, active):
        self.aV22 = active
        self.musicwhite()

    def activeValue23(self, active):
        self.aV23 = active
        self.on_checkbox_active()



    def musicbed(self):
        if self.aV18 == True:
            import lightningstrike

    def musiclab(self):
        if self.aV16 == True:
            import lightningstrike
    def labscreen(self):
        if self.aV17 == True:
            import screen

    def bedscreen(self):
        if self.aV19 == True:
            import screen

    def musicliving(self):
        if self.aV20 == True:
            import lightningstrike

    def musicwhite(self):
        if self.aV22 == True:
            import lightningstrike






    def geofencinglab(self):
        if self.aV12 == True:
            from geofencing import src
            import app

    def geofencingBed(self):
        if self.aV13 == True:
            from geofencing import src
            import app

    def geofencingLiving(self):
        if self.aV14 == True:
            from geofencing import src
            import app

    def geofencingWhite(self):
        if self.aV15 == True:
            from geofencing import src
            import app




    def sunLab(self):
        if self.aV4 == True:
            t1 = datetime.datetime.now()
            if t1.hour >= 8 and t1.hour <= 16:
                self.b.set_light(2, 'on', False)

            elif t1.hour == 7:
                if t1.minute >= 40:
                    self.b.set_light(2, 'on', False)
                else:
                    self.b.set_light(2, 'on', True)

            elif t1.hour == 17:
                if t1.minute <= 45:
                    self.b.set_light(2, 'on', False)
                else:
                    self.b.set_light(2, 'on', True)

            else:
                self.b.set_light(2, 'on', True)
            t = Timer(5, self.sunLab)
            t.start()

        else:

            t = Timer(5, self.sunLab)
            t.cancel()

    def weatherLab(self):
        if self.aV8 == True:
            import weather
            t = Timer(5, self.weatherLab)
            t.start()

        else:
            from phue import Bridge
            b = Bridge('192.168.0.13')
            b.set_light(2,'on', False)

            t = Timer(5, self.weatherLab)
            t.cancel()

    def weatherBed(self):
        if self.aV9 == True:
            import weather
            t = Timer(5, self.weatherBed)
            t.start()

        else:

            from phue import Bridge
            b = Bridge('192.168.0.13')
            b.set_light(1, 'on', False)

            t = Timer(5, self.weatherLab)
            t.cancel()

            t = Timer(5, self.weatherBed)
            t.cancel()

    def weatherLiving(self):
        if self.aV10 == True:
            import weather
            t = Timer(5, self.weatherLiving)
            t.start()

        else:

            t = Timer(5, self.weatherLiving)
            t.cancel()

    def weatherWhite(self):
        if self.aV11 == True:
            import weather
            t = Timer(5, self.weatherWhite)
            t.start()

        else:

            t = Timer(5, self.weatherWhite)
            t.cancel()


    def sunBed(self):
        if self.aV5 == True:
            t1 = datetime.datetime.now()
            if t1.hour >= 8 and t1.hour <= 16:
                self.b.set_light(1, 'on', False)

            elif t1.hour == 7:
                if t1.minute >= 40:
                    self.b.set_light(1, 'on', False)
                else:
                    self.b.set_light(1, 'on', True)

            elif t1.hour == 17:
                if t1.minute <= 45:
                    self.b.set_light(1, 'on', False)
                else:
                    self.b.set_light(1, 'on', True)

            else:
                self.b.set_light(1, 'on', True)
            t = Timer(5, self.sunBed)
            t.start()

        else:

            t = Timer(5, self.sunBed)
            t.cancel()

    def sunLiving(self):
        if self.aV6 == True:
            t1 = datetime.datetime.now()
            if t1.hour >= 8 and t1.hour <= 16:
                self.b.set_light(3, 'on', False)

            elif t1.hour == 7:
                if t1.minute >= 40:
                    self.b.set_light(3, 'on', False)
                else:
                    self.b.set_light(3, 'on', True)

            elif t1.hour == 17:
                if t1.minute <= 45:
                    self.b.set_light(3, 'on', False)
                else:
                    self.b.set_light(3, 'on', True)

            else:
                self.b.set_light(3, 'on', True)
            t = Timer(5, self.sunLiving)
            t.start()

        else:

            t = Timer(5, self.sunLiving)
            t.cancel()


    def sunWhite(self):
        if self.aV7 == True:
            t1 = datetime.datetime.now()
            if t1.hour >= 8 and t1.hour <= 16:
                self.b.set_light(4, 'on', False)

            elif t1.hour == 7:
                if t1.minute >= 40:
                    self.b.set_light(4, 'on', False)
                else:
                    self.b.set_light(4, 'on', True)

            elif t1.hour == 17:
                if t1.minute <= 45:
                    self.b.set_light(4, 'on', False)
                else:
                    self.b.set_light(4, 'on', True)

            else:
                self.b.set_light(4, 'on', True)
            t = Timer(5, self.sunWhite)
            t.start()

        else:

            t = Timer(5, self.sunWhite)
            t.cancel()

    def snowy(self):
        self.nl.set_color(WHITE)
        return

    def rainy(self):
        self.nl.set_color((30, 144, 255))
        return

    def sunny(self):
        self.nl.set_color((ORANGE))
        return

    def cloudy(self):
        self.nl.set_color((135, 206, 235))
        return

    def tempControl(self):
        try:
            if self.aV2 == True and self.nl.get_power() == True:
                url = 'http://api.openweathermap.org/data/2.5/weather?id=5946768&appid=authentication token'#Real token was removed by authors for protecting security
                json_data = requests.get(url).json()
                temp = json_data['main']['temp']
                cel = float(temp) - 273.15
                '''content=GridLayout(cols=1)
                content_admit=Button(text='OK')
                content.add_widget(Label(text='Temperature is: '+str(cel)+'°C'))
                content.add_widget(content_admit)
                popup = Popup(title='Message',content=content,auto_dismiss=False)
                content_admit.bind(on_release=popup.dismiss)
                popup.open()'''
                if (temp >= 303.15):
                    self.extreme()
                elif (temp >= 293.15 and temp < 303.15):
                    self.hot()
                elif (temp >= 283.15 and temp < 293.15):
                    self.medium()
                elif (temp >= 273.15 and temp < 283.15):
                    self.chilly()
                elif (temp >= 263.15 and temp < 273.15):
                    self.cold()
                elif (temp >= 253.15 and temp < 263.15):
                    self.freezing()
                else:
                    pass
                t = Timer(5, self.tempControl)
                t.start()
            else:
                t = Timer(5, self.tempControl)
                t.cancel()
        except AttributeError:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to nanoleaf at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def extreme(self):
        self.nl.set_color(RED)
        return

    def hot(self):
        self.nl.set_color(ORANGE)
        return

    def medium(self):
        self.nl.set_color(YELLOW)
        return

    def chilly(self):
        self.nl.set_color(GREEN)
        return

    def cold(self):
        self.nl.set_color((0, 255, 255))
        return

    def freezing(self):
        self.nl.set_color(BLUE)
        return

    def on_value3(self, brightness):
        self.labValue = "%d" % brightness
        self.b.set_light(2, 'bri', int(self.labValue))

    def on_value4(self, brightness):
        self.bedValue = "%d" % brightness
        self.b.set_light(1, 'bri', int(self.bedValue))

    def on_value5(self, brightness):
        self.livingValue = "%d" % brightness
        self.b.set_light(3, 'bri', int(self.livingValue))

    def on_value6(self, brightness):
        self.whiteValue = "%d" % brightness
        self.b.set_light(4, 'bri', int(self.whiteValue))

    def lab_on(self, *args):
        try:
            self.b.set_light(2, 'on', True)
        except phue.PhueRequestTimeout:
            content = GridLayout(cols=1)
            content.add_widget(Label(text='Please connect to philips  at first'))
            content_admit = Button(text='OK')
            content.add_widget(content_admit)
            popup = Popup(title='Message', content=content, auto_dismiss=False)
            content_admit.bind(on_release=popup.dismiss)
            popup.open()

    def lab_off(self, *args):
        self.b.set_light(2, 'on', False)

    def lab_up(self, *args):
        brightness = self.b.get_light(2, 'bri')
        if self.b.get_light(2, 'on') == True and brightness < 238:
            self.b.set_light(2, 'bri', brightness + 17)

    def lab_down(self, *args):
        brightness = self.b.get_light(2, 'bri')
        if self.b.get_light(2, 'on') == True and brightness > 17:
            self.b.set_light(2, 'bri', brightness - 17)

    def bed_on(self, *args):
        self.b.set_light(1, 'on', True)

    def bed_off(self, *args):
        self.b.set_light(1, 'on', False)

    def bed_up(self, *args):
        brightness = self.b.get_light(1, 'bri')
        if self.b.get_light(1, 'on') == True and brightness < 238:
            self.b.set_light(1, 'bri', brightness + 17)

    def bed_down(self, *args):
        brightness = self.b.get_light(1, 'bri')
        if self.b.get_light(1, 'on') == True and brightness > 17:
            self.b.set_light(1, 'bri', brightness - 17)

    def living_on(self, *args):
        self.b.set_light(3, 'on', True)

    def living_off(self, *args):
        self.b.set_light(3, 'on', False)

    def living_up(self, *args):
        brightness = self.b.get_light(1, 'bri')
        if self.b.get_light(3, 'on') == True and brightness < 238:
            self.b.set_light(3, 'bri', brightness + 17)

    def living_down(self, *args):
        brightness = self.b.get_light(3, 'bri')
        if self.b.get_light(3, 'on') == True and brightness > 17:
            self.b.set_light(3, 'bri', brightness - 17)

    def white_on(self, *args):
        self.b.set_light(4, 'on', True)

    def white_off(self, *args):
        self.b.set_light(4, 'on', False)

    def white_up(self, *args):
        brightness = self.b.get_light(4, 'bri')
        if self.b.get_light(4, 'on') == True and brightness < 238:
            self.b.set_light(4, 'bri', brightness + 17)

    def white_down(self, *args):
        brightness = self.b.get_light(4, 'bri')
        if self.b.get_light(4, 'on') == True and brightness > 17:
            self.b.set_light(4, 'bri', brightness - 17)

    def connect_hue(self, *args):
        self.b = Bridge('192.168.0.13')

    def callback1(self, *args):
        self.disabled = False

    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    TestApp().run()
