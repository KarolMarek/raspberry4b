from flask import Flask, Response
from picamera2 import Picamera2
from libcamera import Transform
import cv2

### Streaming video: http://127.0.0.1:5000/video_feed

app = Flask(__name__)
app.debug = False

size2 = (1640, 1232) #laggi
size1 = (640, 480) # bad
size3 = (800, 600) # bad

raw={'format': 'SBGGR12', 'size': size3}
main={"format": 'XRGB8888', "size": size1}

camera = Picamera2()
camera.configure(camera.create_preview_configuration(main=main, transform=Transform(vflip = True)))
camera.start()

def generate_frames():
    while True:
        frame = camera.capture_array()
        #It writes a JPEG-compressed image into a memory buffer (RAM) instead of to disk
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)