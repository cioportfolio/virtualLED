import virtualLED
from time import sleep
import colorsys
import math

def pix(r,c):
    if c%2==0:
        return c*16+r
    else:
        return (c+1)*16-1-r

def tobyte(v):
    return int(v*255)

def rainbow(hue):
    h=(hue%256)/256
    r,g,b = colorsys.hsv_to_rgb(h,1.0,1.0)
    return (tobyte(r*.9),tobyte(g*.8),tobyte(b))

def l(t):
    return pix(int(math.sin(t*11/180*math.pi)*7.5+8), int(math.cos(t*5/180*math.pi)*7.5+8))

with virtualLED.VirtualLED((16,16)) as vl:
    h=0
    while True:
        vl[l(h-15)]=(0,0,0)
        vl[l(h)]=rainbow(h)
        vl.show()
        h+=1
        sleep(.01)
