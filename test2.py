import time
import numpy as np

from picamera2 import Picamera2, Preview
from matplotlib import pyplot as plt

# RGB_FORMATS = {"BGR888", "RGB888", "XBGR8888", "XRGB8888", "RGB161616", "BGR161616"}
main = {'size': (1640, 1232), 'format': 'XBGR8888'}  # or BGR888

picam2 = Picamera2()
capture_config = picam2.create_still_configuration(main = main)
picam2.configure(capture_config)
picam2.start()
time.sleep(1)

#data8 = picam2.capture_array('main')
#data16 = data8.view(np.uint16)

#plt.imshow(data16, cmap='gray')
#plt.imsave('test2.png', data16) #, cmap='gray'
#picam2.capture_image()
image = picam2.capture_image()
#plt.imsave('test2.jpg', image)
picam2.capture_file("test1.jpg")