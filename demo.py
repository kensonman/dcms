#-*- coding: utf-8 -*-
# Author: Kenson Man <kenson@kenson.idv.hk>
# File: ass1.py
# Desc: The assignment one demo
#       It will prepare the camera and stream it into port 8000
#
import socket
import time
from picamera import PiCamera
from RPi import GPIO

#setup
width=640
height=480
port=8000
pin_yellow=23
pin_red=24

def init():
    print('Initializes the program...')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_yellow, GPIO.OUT)
    GPIO.setup(pin_red, GPIO.OUT)
    
def setready(status):
    print('Setting status: %s'%status)
    GPIO.output(pin_yellow, status)
    GPIO.output(pin_red, not status)
    
init()
setready(True)

# Streaming 
with PiCamera() as camera:
  camera.resolution=(640,480)
  camera.framerate=24
  
  sock=socket.socket()
  sock.bind(('0.0.0.0',8000))
  sock.listen(0)
  
  c=sock.accept()[0].makefile('wb')
  try:
    camera.start_recording(c, format='h264')
    camera.wait_recording(60)
    camera.stop_recording()
  finally:
    c.close()
    sock.close()
    setready(False)
