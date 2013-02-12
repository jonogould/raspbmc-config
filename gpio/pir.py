from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN)

while 1:
	motion = GPIO.input(24)
	print motion
	sleep(0.1)
