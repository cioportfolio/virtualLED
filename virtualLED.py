import pygame as pg
import numpy as np

class VirtualLED:
        
    def __init__(self, leds, brightness=1.0, led_pixel_size=64, background=(63,63,63)):
        pg.init()
        self.bright=brightness
        self.bg=background
        self.lr=led_pixel_size/2.0
        if isinstance(leds, tuple):
            self.rows, self.cols = leds
        else:
            self.rows=1
            self.cols=leds
        self.screen = pg.display.set_mode((self.cols*led_pixel_size*1.1, self.rows*led_pixel_size*1.1))
        pg.display.set_caption("Virtual LEDs")
        self.leds = np.zeros((self.rows, self.cols, 3), dtype=np.uint8)
        self.show()
        
    def __enter__(self):
        return self
    
    def __exit__(self,exc_type, exc_value, traceback):
        pg.quit()
        
    def fade(self, colour):
        r,g,b = colour
        return (r*self.bright, g*self.bright, b*self.bright)
        
    def show(self):
        self.screen.fill(self.bg)
        for r in range(self.rows):
            for c in range(self.cols):
                pg.draw.circle(self.screen, self.fade(self.leds[r,c]), ((c*2+1)*self.lr*1.1,(r*2+1)*self.lr*1.1), self.lr)
        pg.display.flip()

    def __setitem__(self, l, v):
        if self.rows==1:
            self.leds[0][l]=v
        else:
            c=l//self.rows
            r=l%self.rows
            if c%2==0:
                self.leds[r][c]=v
            else:
                self.leds[self.rows-1-r][c]=v
    
    def __len__(self):
        return self.rows*self.cols

    def fill(self, rgb):
        self.leds[:]=rgb
        
    @property
    def brightness(self):
        return self.bright
    
    @brightness.setter
    def brightness(self, b):
        self.bright=b
        
    def deinit(self):
        self.fill((0,0,0))
        self.show()
    
    @property
    def n(self):
        return self.rows*self.cols
    
    def write(self):
        self.show()
        
    
        
        
    
        
        
    
    
        
    