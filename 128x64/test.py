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
f = Font(1)
f.print_string(0,0,"ABCDEFGHIJKLMNOPQRSTU")
f.print_string(0,9,"ABCDEFGHIJKLMNOPQRSTU")
f.print_string(0,18,"ABCDEFGHIJKLMNOPQRSTU")
f.print_string(0,27,"ABCDEFGHIJKLMNOPQRSTU")
f.print_string(0,36,"ABCDEFGHIJKLMNOPQRSTU")
f.print_string(0,44,"ABCDEFGHIJKLMNOPQRSTU")
f.print_string(0,53,"ABCDEFGHIJKLMNOPQRSTU")
dis.update()
sleep(3)

dis.clear()
f = Font(2)
f.print_string(0,0,"ABCDEFGHIJ")
f.print_string(0,18,"ABCDEFGHIJ")
f.print_string(0,36,"ABCDEFGHIJ")
dis.update()
sleep(3)

dis.clear()
f = Font(3)
f.print_string(0,0,"ABCDEFG")
f.print_string(0,27,"ABCDEFG")
dis.update()
sleep(3)

dis.clear()
f = Font(4)
f.print_string(0,0,"ABCDE")
dis.update()
sleep(3)

dis.clear()
f.print_string(0,0,"ABCDE")
dis.set_contrast_control(255)
dis.update()
sleep(3)

dis.clear()
f.print_string(0,0,"ABCDE")
dis.set_contrast_control(10)
dis.update()

#dis.clear()
dis.close()
