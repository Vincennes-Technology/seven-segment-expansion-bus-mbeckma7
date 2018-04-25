#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv
# http://RasPi.tv/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3
import RPi.GPIO as GPIO
import subprocess
import time
import Adafruit_CharLCD as LCD
import ADC0832
import socket

SERVERIP = '10.0.0.43'

GPIO.setmode(GPIO.BCM)
lcd = LCD.Adafruit_CharLCDPlate()
while True:
 IPaddr = subprocess.check_output(['hostname','-I'])
 if len(IPaddr) > 8:
  break
 else:
  time.sleep(2)
Name = subprocess.check_output(['hostname']).strip()
displayText = IPaddr + Name
Select = False
oldmessage = None
# GPIO 23 & 24 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# now we'll define two threaded callback functions
# these will run in another thread when our events are detected


def my_callbackIP(channel):
    global Select
    #print "falling edge detected on 24"
    Select = False


def my_callbackADC(channel):
    global Select
    #print "falling edge detected on 23"
    Select = True

# when a falling edge is detected on port 24, regardless of whatever
# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callbackIP, bouncetime=300)
# when a falling edge is detected on port 23, regardless of whatever
# else is happening in the program, the function my_callback2 will be run
# 'bouncetime=300' includes the bounce control written into interrupts2a.py
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callbackADC, bouncetime=300)
try:
    while True:
        n = 0
        if Select:
            value = ADC0832.getADC(0)
            VoltText = 'current voltage\n %f' % value
            Thismessage = VoltText
        else :
            Thismessage = displayText
        if oldmessage == Thismessage:
            pass
        else:
            lcd.clear()
            lcd.message(Thismessage)
            oldmessage = Thismessage
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# establish socket to talk over ip
            sock.connect((SERVERIP, 8881)) #connect to server IP, port 8881
            print "%d : Connected to server" % n, #tells you if you are connected to server
            data = "'Matts ADC',%d, '%f'" %(n, VoltText) #data to be sent to the server
            sock.sendall(data) # sends all data collected
            print" Sent:", data #data= 'name of data, %d= n, data or value'
            sock.close()
            n += 1
            time.sleep(30) #sleep for 30 sec.
        time.sleep(0.2)


except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
    GPIO.cleanup()           # clean up GPIO on normal exit