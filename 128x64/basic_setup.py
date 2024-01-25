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
dis.close()
