# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 2231puppy
#
# SPDX-License-Identifier: Unlicense

# Imports
import time
import board
import digitalio
import robocloudlib

# Pass the digitalio and board instances so the class can control pins.
motors = robocloudlib.Motors(digitalio, board)

# Motor 1 FWD, Motor 2 FWD
motors.set_speeds(1, 1)

time.sleep(0.5)

# Motor 1 BACKWD, Motor 2 BACKWD
motors.set_speeds(-1, -1)

time.sleep(0.5)

# Motor 1 OFF, Motor 2 OFF
motors.set_speeds(0, 0)
