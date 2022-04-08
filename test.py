import requests
import time
import os

def create_file(name_file):
    try:
        folder_name = name_file 
        os.mkdir(folder_name)
    except:
        pass  

def download_frame(frame):
    create_file('image')
    for i in range(frame):
        image_url = "http://192.168.4.1/jpg"
        r = requests.get(image_url).content
        with open(f"image/images{i}.jpg", "wb+") as f:
            f.write(r)
        print(f"download {i+1} image")
        time.sleep(3)
    print('Done')
    
download_frame(6)