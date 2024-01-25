#!/usr/bin/env python3

from oled import OLED, Font, Graphics
from time import sleep

dis = OLED(1)

dis.begin()
dis.initialize()

dis.set_memory_addressing_mode(0)
dis.set_column_address(0, 127)
dis.set_page_address(0, 7)

dis.deactivate_scroll()

dis.clear()
f = Font(3)
f.print_string(0,0,"ABCDE")
f.print_string(0,27,"ABCDE")
dis.update()
f = Font(1)
f.print_string(73,57,"Status: H")
dis.update()
sleep(3)
dis.clear()
f.print_string(73,57, "Status: O")
dis.update()
sleep(3)
dis.clear()
f.print_string(73,57,"Status: W")
dis.update()
sleep(3)
dis.clear()
f.print_string(73,57,"Status: S")
dis.update()
sleep(3)
dis.clear()
f.print_string(73,57,"Status: R")
dis.update()
sleep(3)
dis.clear()





#Graphics.draw_circle(64,59,4)
dis.update()
#f.print_char(0,53,42)
#dis.update()
#sleep(3)

dis.close()
