# From http://www.scraptopower.co.uk/misc/raspberry-pi-led-sequencer

import RPi.GPIO as GPIO
import time

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)

sleeptimer = 0.1
allon = 1
quit = 1

while quit == 1:
	GPIO.output(10, False)
	GPIO.output(3, True)
	time.sleep(sleeptimer)

	GPIO.output(3, False)
	GPIO.output(5, True)
	time.sleep(sleeptimer)

	GPIO.output(5, False)
	GPIO.output(7, True)
	time.sleep(sleeptimer)

	GPIO.output(7, False)
	GPIO.output(8, True)
	time.sleep(sleeptimer)

	GPIO.output(8, False)
	GPIO.output(10, True)
	time.sleep(sleeptimer)

	quit = GPIO.input(11)
	allon = GPIO.input(12)

	while allon == 0:
GPIO.output(3, True)
    	GPIO.output(5, True)
    		GPIO.output(7, True)
    	GPIO.output(8, True)
    		GPIO.output(10, True)
    	allon = GPIO.input(12)
   
	GPIO.output(3, False)
GPIO.output(5, False)
GPIO.output(7, False)
	GPIO.output(8, False)
GPIO.output(10, False)

GPIO.output(3, False)
GPIO.output(5, False)
GPIO.output(7, False)
GPIO.output(8, False)
GPIO.output(10, False)
