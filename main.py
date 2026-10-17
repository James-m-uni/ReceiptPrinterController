import tkinter as tk
import time

import posPrinter.posPrinter as pr

printer = pr.PosPrinter(0x2730, 0x1004)
printer.initialise()
time.sleep(1)
printer.write_text("Hello World")
printer.write_text("Hello World")
printer.write_text("Hello World")
printer.write_text("Hello World")



