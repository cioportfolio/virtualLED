import virtualLED
from time import sleep

with virtualLED.VirtualLed((8,32)) as vl:
    for i in range(20):
        vl[i]=(255,0,0)
        vl.show()
        sleep(.2)
