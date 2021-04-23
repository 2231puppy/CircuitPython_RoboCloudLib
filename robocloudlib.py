# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Micha for Project Stida
#
# SPDX-License-Identifier: MIT
"""
`robocloudlib`
================================================================================

Assorted functions specific to the RoboCloud microcontroller by 2231puppy


* Author(s): Micha

Implementation Notes
--------------------

**Hardware:**

RoboCloud

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/2231puppy/Projectstida_CircuitPython_robocloud.git"


class Motors:
    """Motor control class for the RoboCloud"""

    def __init__(self, digitalio, board):
        self.pwma = digitalio.DigitalInOut(board.IO13)
        self.pwmb = digitalio.DigitalInOut(board.IO12)
        self.ina1 = digitalio.DigitalInOut(board.IO14)
        self.ina2 = digitalio.DigitalInOut(board.IO15)
        self.inb1 = digitalio.DigitalInOut(board.IO16)
        self.inb2 = digitalio.DigitalInOut(board.IO17)
        self.pwma.direction = digitalio.Direction.OUTPUT
        self.pwmb.direction = digitalio.Direction.OUTPUT
        self.ina1.direction = digitalio.Direction.OUTPUT
        self.ina2.direction = digitalio.Direction.OUTPUT
        self.inb1.direction = digitalio.Direction.OUTPUT
        self.inb2.direction = digitalio.Direction.OUTPUT

    def set_speeds(self, motora, motorb):
        """Set speeds for both motors. If speed is 0, it will stop.
        Takes 2 arguments: Motor A speed and Motor B speed"""
        if motora:
            self.pwma.value = True
        if motorb:
            self.pwmb.value = True
        if motora > 0:
            self.ina1.value = True
            self.ina2.value = False
        elif motora < 0:
            self.ina1.value = False
            self.ina2.value = True
        elif motora == 0:
            self.ina1.value = False
            self.ina2.value = False
        if motorb > 0:
            self.inb1.value = True
            self.inb2.value = False
        elif motorb < 0:
            self.inb1.value = False
            self.inb2.value = True
        elif motorb == 0:
            self.inb1.value = False
            self.inb2.value = False
