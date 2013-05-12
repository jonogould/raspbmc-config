raspbmc-config
==============

My raspbmc files that do various things.


### Install image to SD card

Easy installer: http://alltheware.wordpress.com/2012/12/11/easiest-way-sd-card-setup/


### gPhoto2

Allows you to take photos with your camera via terminal

```apt-get install gphoto2```

See usbreset.c if you get an error saying that the usb device is already in use..


### GPIO

[gpio cheat sheet](https://www.dropbox.com/s/m5l185qxq9w5mzk/raspberry-pi-gpio-cheat-sheet.jpg)

[elinux](http://elinux.org/RPi_Low-level_peripherals)

	sudo apt-get update
	sudo apt-get install python-dev
	sudo apt-get install python-rpi.gpio
