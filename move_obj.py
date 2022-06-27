import sort_path
import numpy as np
import cv2
from time import sleep
import random
from CAR_ESP import Data_port

lost_move = ''

def draw_obj(img,list_pos,color):
    start_X= round(list_pos[0]*100/35*10)
    start_Y= round(list_pos[1]*100/35*10)
    end_X=start_X+35
    end_Y= start_Y+35
    start_point = (start_X, start_Y)
    end_point = (end_X, end_Y)
    thickness = -1
    return cv2.rectangle(img, start_point, end_point, color, thickness)

def main(name = None ,lost_move =lost_move):
    if name == None:
        name = f"image {random.randrange(0,10)}"
    path, pos = sort_path.get_path()
    height = 350
    width = 350
    img = np.zeros((height,width,3), np.uint8)
    img[:,:] = (0,0,0)

    img = draw_obj(img,pos[0],(255, 0, 0))
    img = draw_obj(img,pos[1],(0, 0, 255))
    img = draw_obj(img,pos[2],(0, 255 , 0))
    
    lost = 0
    cont = 0
    x,y = pos[1]
    for i in path:
        img = np.zeros((height,width,3), np.uint8)
        img = draw_obj(img,pos[0],(0, 0, 255))
        img = draw_obj(img,pos[2],(0, 255 , 0))
        if lost == 0 :
            lost = i
            img = draw_obj(img,pos[1],(255, 0, 0))
            cv2.imshow(name,img)
            cv2.waitKey(1)
            on_loop = 1
            while on_loop:
               on_loop = int(input(" Enter 1 to start or 0 to end >> "))
               if on_loop == 1:
                   on_loop = 0
               elif on_loop == 0 :
                   on_loop = 1
                   break
            if on_loop == 1:
                break
            continue
        
        if  i[0] > lost[0]:
            # if lost_move == 'R':
            #     Data_port.set_data(b'F')
            # else:
            #     lost_move = 'R'
            #     Data_port.set_data(b'R')
            #     sleep(1)
            #     Data_port.set_data(b'F')
            x += 1
            img = np.zeros((height,width,3), np.uint8)
            img = draw_obj(img,pos[0],(0, 0, 255))
            img = draw_obj(img,pos[2],(0, 255 , 0))
            img = draw_obj(img,(x,y),(255, 0, 0))
        if i[0] < lost[0]:
            # if lost_move == 'R':
            #     Data_port.set_data(b'F')
            # else:
            #     lost_move = 'R'
            #     Data_port.set_data(b'R')
            #     sleep(2)
            #     Data_port.set_data(b'F')
            lost_move = ''
            x -= 1
            img = np.zeros((height,width,3), np.uint8)
            img = draw_obj(img,pos[0],(0, 0, 255))
            img = draw_obj(img,pos[2],(0, 255 , 0))
            img = draw_obj(img,(x,y),(255, 0, 0))
        if  i[1] > lost[1]:
            # if lost_move == 'L':
            #     Data_port.set_data(b'F')
            # else:
            #     lost_move = 'L'
            #     Data_port.set_data(b'L')
            #     sleep(2)
            #     Data_port.set_data(b'F')
            y += 1
            img = np.zeros((height,width,3), np.uint8)
            img = draw_obj(img,pos[0],(0, 0, 255))
            img = draw_obj(img,pos[2],(0, 255 , 0))
            img = draw_obj(img,(x,y),(255, 0, 0))
        if i[1] < lost[1]:
            # if lost_move == 'L':
            #     Data_port.set_data(b'F')
            # else:
            #     lost_move = 'L'
            #     Data_port.set_data(b'L')
            #     sleep(1)
            #     Data_port.set_data(b'F')
            y -= 1
            img = np.zeros((height,width,3), np.uint8)
            img = draw_obj(img,pos[0],(0, 0, 255))
            img = draw_obj(img,pos[2],(0, 255 , 0))
            img = draw_obj(img,(x,y),(255, 0, 0))
        cv2.imshow(name,img)
        cv2.waitKey(1)
        cont += 1
        print(f"{name} , step : {cont} , position : {x,y} ")
        # Data_port.set_data(b'S')
        sleep(1)
        lost = i
        
if __name__ == "__main__":
    main()