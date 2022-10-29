import picamera
import  pyshine as ps

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

# This function init local server, camera and runs them.
def start_streaming():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps,HTML)
    address = ('192.168.1.142',8000)
    StreamProps.set_Mode(StreamProps,'picamera')    
    with picamera.PiCamera(resolution='640x480', framerate=30) as camera:
        output = ps.StreamOut()
        StreamProps.set_Output(StreamProps,output)
        camera.rotation = 180 # My PiCamera is rotated 180º.
        camera.brightness = 60 # Dark house, had to increase brightness.
        camera.start_recording(output, format='mjpeg')
        server = ps.Streamer(address, StreamProps)
        print('Server started at','http://'+address[0]+':'+str(address[1]))
        server.serve_forever()

if __name__=='__main__':
    start_streaming()