#show IP address on the LCD Plate at startup
#
import subprocess
import time
import Adafruit_CharLCD as LCD

logfile = open("LCDDisplay.log", 'a')
lcd = LCD.Adafruit_CharLCDPlate()
while True:
	IPaddr = subprocess.check_output(['hostname','-I'])
	if len(IPaddr) > 8:
		break
	else:
		time.sleep(2)
Name = subprocess.check_output(['hostname']).strip()
displayText = IPaddr + Name
currentTime = "Running @ " + time.strftime("%c") + ":\n"
logfile.write(currentTime)
logfile.write(displayText)
lcd.clear()
lcd.message(displayText)
logfile.close()
