import cv2
import numpy as np
import glob

def make_video ():
    img_array = []
    for filename in glob.glob('./motion_feed/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    out = cv2.VideoWriter('./video/video.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 10, size)
 
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()