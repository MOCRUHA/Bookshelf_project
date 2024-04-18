import os
import shutil

import cv2
import requests as req
import mysql.connector

from utils import move_imgs, isbn_image_decoder, inject_db, api_isbn


#functions to import: img_to_decode(path), move_imgs(src, dst)


#dir where imgs are kept
DIR = r'C:\Users\gusta\Documents\OG'
USE_DIR = r'C:\Users\gusta\Documents\USE'

#copy and rename imgs to use dir
move_imgs.move_img(DIR, USE_DIR)

#return isbn number from images
ISBN = []

for image in os.listdir(USE_DIR):
	img = f'{USE_DIR}\\{image}'

	ISBN.append(isbn_image_decoder.img_to_code(img))

with open('isbns.txt', 'w') as f:
	for item in ISBN:
		f.write(item)
		f.write('\n')

#send each isbn to isbn API and save the response (maybe filter it?)
for id in ISBN:
	inject_db.data_to_db(api_isbn.isbn_api_call(id))


