import random

comments = {"motion": ["Por aquí ando perris!", "Mira que yaski.", "Er gato al aparato.", "Illo que pasa venid ya."],
            "stream": ["Abro stream! http://192.168.1.142:8000", "Illo seguirme en el Twitch: http://192.168.1.142:8000", "Darme dinero: http://192.168.1.142:8000"],
            "video": ["Ahi va mi último clip!", "Mira la pila werta que he dao.", "Dale like ome.", "Mamá que estoy bien.."],
            "foto": ["Quien anda ahí!", "Serfie!", "Sargo wapo?", "Para ya paparazzi."]
            }

def motion_comment():
    comment = random.choice(comments["motion"])
    return comment

def stream_comment():
    comment = random.choice(comments["stream"])
    return comment

def video_comment():
    comment = random.choice(comments["video"])
    return comment

def photo_comment():
    comment = random.choice(comments["foto"])
    return comment