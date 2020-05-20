#/usr/bin/env python3
"""
Open-Source and moddable flappy remake in python3
By Kane Cross, 20 May 2020
V0.0.01-dev - 20 May 2020
Notes:
 V0.0.01-dev:
  - Add threading
"""
#Imports
import threading #For later use
import tkinter
import random
import time
import sys #For later use

#External
from Bird import *
from Spike import *
from Level import *

#Developer Stuff
Logging = False #Too much effort at the moment lol
ShowFPS = True
Threading = False

#Functions
pass

#Variables
ResW = 500 #px
ResH = 500 #px
FPS = 50 #0.02sec per frame
PIPS = 100 #Physics calculation every 0.01sec

#Main
Canvas = tkinter.Canvas(ResW, ResH, bg="#000000")
Canvas.pack(expand=YES, fill=BOTH) #Canvas.pack() is fine, I just like stability
BirdImage = tkinter.PhotoImage(file=Bird.Image)
Canvas.create_image(50, 10, image=BirdImage, anchor=NW) #Testing
Canvas.update()

#StartScreen


#Game


#Restart/End


#Cleanup
quit()
MainWindow.destroy()
