import sys
import time

print "Blinking User LED"
print "Enter CTRL+C to exit"

def ledon():
        value = open("/sys/class/leds/white:ph11:led3/brightness","w")
        value.write(str(1))
        value.close()

def ledoff():
        value = open("/sys/class/leds/white:ph11:led3/brightness","w")
        value.write(str(0))
        value.close()

while True:
        ledon()
        time.sleep(.01)
        ledoff()
        time.sleep(.5)

