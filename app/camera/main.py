import picamera
import pyshine as ps

# Camera Setup
camera = picamera.PiCamera(resolution = "640x480", framerate=30)
camera.rotation = 180
camera.brightness = 60

# Basic HTML solution to stream the mjpg captured from PiCamera (not a front end guy as you can see..).
HTML="""
<html>
<head>
<title>PumuKam</title>
</head>
<body>
<center><h1> Pumuky en riguroso directo </h1></center>
<center><img src="stream.mjpg" width='640' height='480' autoplay playsinline></center>
</body>
</html>
"""

# Stream Setup
StreamProps = ps.StreamProps
StreamProps.set_Page(StreamProps,HTML)
address = ('192.168.1.142',8000)
StreamProps.set_Mode(StreamProps,'picamera')

# This function init local server, camera and runs them.
def start_streaming():
    output = ps.StreamOut()
    StreamProps.set_Output(StreamProps,output)
    camera.start_recording(output, format='mjpeg')
    server = ps.Streamer(address, StreamProps)
    print('Server started at','http://'+address[0]+':'+str(address[1]))
    server.serve_forever()

# Captures an image and saves it in the introduced path
def capture(path):
    camera.capture(path)
