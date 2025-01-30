#!/bin/env python3 

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from time import sleep


serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
with canvas(device) as draw:
    draw.text((0, 0), "T: 66.6", fill="white")
sleep(5)
