import cv2
import numpy as np
import random

def draw_obj(img,list_pos,color):
    while 1:
        start_X= int(random.randrange(0,315,35))
        start_Y= int(random.randrange(0,315,35))
        end_X=start_X+35
        end_Y= start_Y+35
        if not [(start_X, start_Y),(end_X, end_Y)] in list_pos:
            break
    list_pos.append([(start_X, start_Y),(end_X, end_Y)])
    start_point = (start_X, start_Y)
    end_point = (end_X, end_Y)
    thickness = -1
    return cv2.rectangle(img, start_point, end_point, color, thickness) ,list_pos

def creat():
    height = 350
    width = 350
    img = np.zeros((height,width,3), np.uint8)

    img[:,:] = (0,0,0)
    pos = []

    img ,pos= draw_obj(img,pos,(0, 0, 255))
    img ,pos= draw_obj(img,pos,(255, 0, 0))
    img ,pos= draw_obj(img,pos,(0, 255, 0))

    pos_list = []
    for i in pos:
        for j in i:
            pos_list.append((round((j[0]/10)*35/100),round((j[1]/10)*35/100)))
            break

    return pos_list

if __name__ == "__main__":
    creat()