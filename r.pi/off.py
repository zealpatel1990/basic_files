# this script works for python 2 and python 3 ONLY ON RASPBERRY PI
import RPi.GPIO as GPIO
def off():
	import sys
	# below line is for people who are using openelec or similar os for media pupose as well as for other purpose
	#you don't have to worry about is you are using raspbian
	sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib/')
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BOARD)
	for x in range(0,41):
		try:
			GPIO.setup(x,GPIO.OUT)
			GPIO.output(x,0)
		except:
			continue
	GPIO.cleanup()
	print ("All GPIO pins are turned Off.")

off()
