#!usr/bin/python
#https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
#modified by mbeckma7
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(25, GPIO.OUT)

p = GPIO.PWM(12, 50)  # channel=25 frequency=50Hz
p.start(0)
try:
    while True:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()