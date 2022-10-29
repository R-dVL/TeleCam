import random

motion = ["Por aquí ando perris!", "Mira que yaski.", "Er gato al aparato.", "Illo que pasa venid ya."]
stream = ["Abro stream!", "Illo seguirme en el Twitch.", "Darme dinero."]
video = ["Ahi va mi último clip!", "Mira la pila werta que he dao.", "Dale like ome.", "Mamá que estoy bien.."]
foto = ["Quien anda ahí!", "Serfie!", "Sargo wapo?", "Para ya paparazzi."]

def motion_comment():
    comment = random.choice(motion)
    return comment

def stream_comment():
    comment = random.choice(stream)
    return comment

def video_comment():
    comment = random.choice(video)
    return comment

def photo_comment():
    comment = random.choice(foto)
    return comment