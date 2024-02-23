# Virtual LED

## Overview

Python module using pygame graphics to simulate strips or grids of programmable LEDS (e.g. neopixels). It is a virtual drop in for the neopixel driver class.

## Usage

```python
# Simulate a strip of LEDs

import virtualLED
from time import sleep

with virtualLED.VirtualLED(10) as strip:
    for i in range(10):
        strip[i]=(255,0,0)
        strip.show()
        sleep(.2)

```

```python
# Simulate a grid of LEDs. 
# Assumes typical wiring:
# - rows linked together into one list
# - alternate rows reversed

import virtualLED
from time import sleep

with virtualLED.VirtualLED((8,32)) as grid:
    for i in range(10):
        grid[i]=(255,0,0)
        grid.show()
        sleep(.2)

```

