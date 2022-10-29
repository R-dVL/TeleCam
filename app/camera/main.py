from .setup import *

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
