from picamera2 import Picamera2
from picamera2.encoders import H264Encoder,Quality


size1 = (1920, 1080)
size2 = (640, 480)
size3 = (3280, 2464)
picam2 = Picamera2()
vidio_config = picam2.create_video_configuration(main={"size": size2},controls={'FrameRate': 50})
picam2.start_and_record_video("test.mp4", quality = Quality.HIGH, config=vidio_config, duration=10, show_preview=True, audio=False)