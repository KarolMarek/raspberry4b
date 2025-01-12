#!/usr/bin/python3

# Use the configuration structure method to do a full res capture.

import time

from picamera2 import Picamera2

picam2 = Picamera2()
size3 = (3280, 2464)
# We don't really need to change anyhting, but let's mess around just as a test.
picam2.preview_configuration.size = size3
picam2.preview_configuration.format = "YUV420"
#picam2.still_configuration.format = "YUV420"
picam2.still_configuration.size = size3
picam2.still_configuration.enable_raw()
picam2.still_configuration.raw.size = picam2.sensor_resolution

picam2.start("preview", show_preview=False)
time.sleep(2)
print("Now")
picam2.switch_mode_and_capture_file("still", "test_full.jpg")