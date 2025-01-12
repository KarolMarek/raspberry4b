import cv2
from picamera2 import Picamera2, Preview

picam2 = Picamera2(verbose_console=0)
picam2.configure(picam2.create_preview_configuration(main={'format': 'RGB888', 'size': (640, 480)}))
picam2.start_preview(Preview.NULL)
picam2.start()
#picam2.set_controls({'AfMode': 1, 'AfTrigger': 1}) # Continuous autofocus

cv2.startWindowThread()
cv2.namedWindow('Camera', flags=cv2.WINDOW_GUI_NORMAL) # Mandatory to hide CV2 toolbar
while True:
    im = picam2.capture_array()
    cv2.imshow("Camera", im)
    cv2.waitKey(1)

cv2.destroyAllWindows()