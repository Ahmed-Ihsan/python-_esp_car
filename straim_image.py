from bs4 import *
from matplotlib import image
import requests
import os

# CREATE FOLDER
def folder_create(images):
	try:
		folder_name = 'image'
		os.mkdir(folder_name)
	except:
		pass
	download_images(images, folder_name)


def download_images(images, folder_name):
	count = 0
	print(f"Total {len(images)} Image Found!")
	if len(images) != 0:
		for i, image in enumerate(images):
			try:
				image_link = image["data-srcset"]
			except:
				try:
					image_link = image["data-src"]
				except:
					try:
						image_link = image["data-fallback-src"]
					except:
						try:
							image_link = image["src"]
							print(image_link)
						except:
							pass
			try:
				r = requests.get(image_link).content
				try:
					r = str(r, 'utf-8')
				except UnicodeDecodeError:
					with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
						f.write(r)
					count += 1
			except:
				pass
		if count == len(images):
			print("All Images Downloaded!")
		else:
			print(f"Total {count} Images Downloaded Out of {len(images)}")

def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img')
    folder_create(images)

url = 'https://www.google.com/search?q=image+cat&source=lnms&tbm=isch&sa=X&ved=2ahUKEwis0fGUyOT2AhV0hf0HHXAfDfEQ_AUoAXoECAEQAw&biw=1366&bih=657&dpr=1'
main(url)
