#-*- coding: utf-8 -*-
# Author: Kenson Man <kenson@kenson.idv.hk>
# File: ass1.py
# Desc: The assignment one demo
#       It will prepare the camera and stream it into port 8000
#
import socket, time, thread, logging
from picamera import PiCamera
from RPi import GPIO

#setup
logging.basicConfig(filename='dcms.log',level=logging.DEBUG)
logger=logging.getLogger('dcms')
bind='0.0.0.0'
width=640
height=480
framerate=24
port=8000
pin_yellow=23
pin_red=24
pin_btn=25
global recording
recording=False

def init():
    logging.info('Initializes the program...')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_yellow, GPIO.OUT)
    GPIO.setup(pin_red, GPIO.OUT)
    GPIO.setup(pin_btn, GPIO.IN)
    
def setready(status):
    logging.info('Setting status: %s'%status)
    GPIO.output(pin_yellow, status)
    GPIO.output(pin_red, not status)

def checkbtn():
	'''
	Check an change btn status
	'''
	global recording
	while True:
		if GPIO.input(pin_btn)==1:
			logging.info('Captured btn clicked')
			recording=not recording
			if recording:
				thread.start_new_thread(stream, ())
			time.sleep(3)
		time.sleep(0.5)

def stream():
	global recording
	if not recording: return
	setready(False)
	# Streaming 
	with PiCamera() as camera:
		camera.resolution=(width,height)
		camera.framerate=framerate

		sock=socket.socket()
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind((bind, port))
		sock.listen(0)

		conn=sock.accept()[0].makefile('wb')
		try:
			camera.start_recording(conn, format='h264')
			while recording:
				logging.info('recording')
				camera.wait_recording(1)
			camera.stop_recording()
		finally:
			conn.close()
			sock.close()
			logging.debug('Closed Socket')
			setready(True)
    
init()
setready(True)
checkbtn()
