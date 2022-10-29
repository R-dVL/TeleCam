# TeleCam
*Raspberry Pi project used to spy my cat.*

## Functions
The RPi will start a local webserver to stream the camera while the PIR sensor is monitoring if any motion is detected to notify it via Telegram Bot with messages and photos.

The Telegram Bot will reply to some commands:
- start: Just used to see if bot is online.
- help: Display commands and some information such as livecam IP.
- foto: Takes and sends back a photo.

## Material
This project uses:
- Raspberry Pi (tested and working in RPi 3B+).
- Picamera (migrating to OpenCV and Flask for major compatibility).
- PIR Sensor.

## Program
The program is divided in submodules:
- bot: Bot submodule, with setup, methods and replies to incoming messages.
- camera: Camera setup and methods to stream and capture.
- config: Setup methods and JSON with configuration information.
- random_reply: This module is made just to add the bot some personality.

## Libraries
### Standard
- Random
- Time
- Threading
- Json
### Raspberry
- PiCamera
- GPIOZero

### Open Source
- Telegram Bot
$ pip install python-telegram-bot

- OpenCV
$ pip install opencv-python

- Pyshine
$ pip install pyshine

--------------------------------------------

*Tested in RPi 3B+*