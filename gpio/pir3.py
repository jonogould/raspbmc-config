from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

sensor_number = 24
GPIO.setup(sensor_number, GPIO.IN)


#while 1:
#	motion = GPIO.input(sensor_number)
#
#	GPIO.set_falling_event(sensor_number)
#	sleep(5)
#	if GPIO.event_detected(sensor_number):
#		print('YES')
#	else:
#		print('NO')

sleep(0.1)

for chan in range(54):
	f = GPIO.gpio_function(chan)
	if f == GPIO.IN:
		func = 'INPUT'
	elif f == GPIO.OUT:
		func = 'OUTPUT'
	elif f == GPIO.ALT0:
		func = 'ALT0'
	else:
		func = 'UNKNOWN'
	print('chan=%s func=%s'%(chan,func))
