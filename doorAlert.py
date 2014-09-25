__author__ = 'hellhammer'

import time
import Adafruit_BBIO.GPIO as GPIO
from emailer import alertMe

GPIO.setup("P8_11", GPIO.IN)

alertTime = 0

while True:
    if not GPIO.input("P8_11"):
        if alertTime == 0:
            alertTime = time.time() + 60
            print "Tuere offen. Warnung in 60 Sekunden, wenn sie offen bleibt."
        else:
            if time.time() > alertTime:
                alertMe("Warnung!", "Die Tuer ist schon lange offen..")
                print("Tuer wurde ueber 60sek geoeffnet. E-Mail verschickt")
                while GPIO.input("P8_11"):
                    time.sleep(.1)
    else:
        alertTime = 0
    time.sleep(.01)