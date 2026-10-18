import tkinter as tk
import time

import posPrinter.posPrinter as pr

printer = pr.PosPrinter(0x2730, 0x1004)
printer.initialise()
time.sleep(1)
printer.write_text("I wish to have a Nissan Skyline R34 when im older. I wish to own and be able to drive it when I want.")


printer.paper_cut()




