#!/usr/bin/env python
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import subprocess
import time

lcd = LCD.Adafruit_CharLCDPlate()
channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def alert(ev=None):
	lcd.clear()
	lcd.message('Tilt Detected')

def loop():
    	GPIO.add_event_detect(channel, GPIO.FALLING, callback=alert)
        while True:
            pass

if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		GPIO.cleanup()