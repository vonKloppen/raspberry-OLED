#!/usr/bin/env python3

from oled import OLED
from oled import Font
from oled import Graphics
from time import sleep

dis = OLED(1)
dis.begin()
dis.initialize()
dis.set_memory_addressing_mode(0)
dis.set_column_address(0, 127)
dis.set_page_address(0, 7)
dis.deactivate_scroll()
dis.clear()

menuPos = 1
numSensors = 2

sensor1Temp = 24.5
sensor1Hum = 55.5
sensor2Temp = 25.6
sensor2Hum = 56.6

menuTitle = {

        "menu1": "Sensor 1",
        "menu2": "Sensor 2",
        "menu3": "Light",
        "menu4": "Camera",
        "menu5": "Options",
        "menu6": "Power"
        }

def loopStatus():

    for sensor in range (1, numSensors + 1):

        title = "menu" + str(sensor)
        dis.clear()
        f = Font(1)
        f.print_string(0 ,0 , menuTitle[title])

        if sensor == 1:

            temp = "Temp: " + str(sensor1Temp) 
            hum = "Hum: " + str(sensor1Hum)

        else:

            temp = "Temp: " + str(sensor2Temp) 
            hum = "Hum: " + str(sensor2Hum)
    
        f = Font(2)
        f.print_string(0, 20, temp)
        f.print_string(0, 46, hum)
        dis.update()
        sleep(5)

while True:

    loopStatus()

dis.close()
