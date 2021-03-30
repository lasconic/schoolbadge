#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522
import subprocess
import os, random

mediaFile = 'giphy.mp4'
mediaDir = 'media/'
reader = SimpleMFRC522()

#print("Hold a tag near the reader")
blackscreen = subprocess.Popen(['feh', '-F', 'black.png'])

try:
    while True:
        try:
            id, text = reader.read()
            print(id)
            print(text)
            mediaFile = random.choice(os.listdir(mediaDir))
            mediaFilePath = os.path.join(mediaDir, mediaFile)
            print(mediaFilePath)
            process = subprocess.call(['cvlc', '--no-osd', '--fullscreen', mediaFilePath,'vlc://quit'])
        finally:
            GPIO.cleanup()
except KeyboardInterrupt:
    blackscreen.terminate()
    exit()
