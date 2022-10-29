import picamera

# Camera Setup
camera = picamera.PiCamera(resolution = "1920x1080")
camera.rotation = 180
camera.brightness = 60

def capture(path):
    camera.capture(path)

