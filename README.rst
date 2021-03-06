Introduction
============


.. image:: https://readthedocs.org/projects/circuitpython-robocloudlib/badge/?version=latest
    :target: https://circuitpython-robocloudlib.readthedocs.io/
    :alt: Documentation Status


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/2231puppy/CircuitPython_RoboCloudLib/workflows/Build%20CI/badge.svg
    :target: https://github.com/2231puppy/CircuitPython_RoboCloudLib/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython driver for 2231puppy's RoboCloud MCU board


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Usage Example
=============

.. code-block:: python

	# Imports
	import board
	import digitalio
	import robocloudlib

	# Pass the digitalio and board instances so the class can control pins.
	motors = robocloudlib.Motors(digitalio, board)

	# Motor 1 FWD, Motor 2 OFF
	motors.set_speeds(1, 0)

	# Motor 1 OFF, Motor 2 BACKWD
	motors.set_speeds(0, -1)

	#Motor 1 OFF, Motor 2 OFF
	motors.set_speeds(0, 0)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/2231puppy/CircuitPython_RoboCloudLib/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
