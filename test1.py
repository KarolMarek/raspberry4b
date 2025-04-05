import time
import numpy as np

from picamera2 import Picamera2, Preview
from matplotlib import pyplot as plt

tuning = Picamera2.load_tuning_file("imx477_noir.json")
picam2 = Picamera2(tuning=tuning)
raw={'format': 'SBGGR12', 'size': (1640, 1232)}
lores = {'size': (1640, 1232), 'format': 'YUV420'} 
controls = {'FrameRate': 80}

config = picam2.create_still_configuration(raw=raw, lores=lores, controls=controls) # YUV420 SBGGR12
picam2.configure(config)
print('Sensor configuration:', picam2.camera_configuration()['sensor'])
print('Stream Configuration:', picam2.camera_configuration()['raw'])
print('Stream Configuration:', picam2.camera_configuration()['lores'])

picam2.start()
print("I do work")
#time.sleep(2)

#nn = picam2.capture_request()
#yuv = nn.make_array('lores')

data8 = picam2.capture_array('raw')
data16 = data8.view(np.uint16)

#plt.imshow(data16, cmap='gray')
plt.imsave('test1.png', data16, cmap='gray') #, cmap='gray'
#plt.imsave('test2.png', yuv, cmap='gray')
print("sss")
picam2.stop()