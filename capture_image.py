#!/usr/bin/python3

# Use the configuration structure method to do a full res capture.

import time

from picamera2 import Picamera2

picam2 = Picamera2()

# We don't really need to change anyhting, but let's mess around just as a test.

capture_config = picam2.create_still_configuration(main={"size":(3280, 2464)})
picam2.configure(capture_config)

# picam2.still_configuration.format = "YUV420"
# picam2.still_configuration.size = (3280, 2464)
# picam2.still_configuration.enable_raw()
#picam2.still_configuration.raw.size = picam2.sensor_resolution

picam2.start()

#capture_file
picam2.capture_file("test_full.jpg")