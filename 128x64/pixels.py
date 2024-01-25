#!/usr/bin/env python3

from oled import OLED
from oled import Font
from oled import Graphics
from time import sleep
import random

dis = OLED(1)
dis.begin()
dis.initialize()
dis.set_memory_addressing_mode(0)
dis.set_column_address(0, 127)
dis.set_page_address(0, 7)
dis.deactivate_scroll()

g = Graphics

while True:

    for count in range (8192):

        random.seed()
        g.draw_pixel(random.randint(0,127),random.randint(0,63),random.randint(0,1))
        dis.update()

#    sleep(50)
#    dis.clear()

dis.close()
