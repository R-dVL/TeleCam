from gpiozero import MotionSensor


pir = MotionSensor(4)

def detection():
    while True:
        pir.wait_for_motion()
        yield 1
        pir.wait_for_no_motion()
        yield 0
if __name__ == "__main__":
    detection()