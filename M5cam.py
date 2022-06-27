import requests
import time
import os

def create_file(name_file):
    try:
        folder_name = name_file 
        os.mkdir(folder_name)
    except:
        pass  

def download_frame(delay = 0):
    create_file('image')
    while 1 :
        image_url = "http://192.168.4.1/jpg"
        r = requests.get(image_url).content
        with open(f"image/images{i}.jpg", "wb+") as f:
            f.write(r)
        print(f"download {i+1} image")
        time.sleep(delay)
    print('Done')
    
# download_frame(6)
