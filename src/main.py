
import os
import shutil

from pyzbar.pyzbar import decode
import requests as req
import mysql.connector
import cv2

from utils import *

def main():
	#dir where imgs are kept
	DIR = r'/home/poly/Dropbox/mobile_imgs'
	USE_DIR = r'/home/poly/Desktop/pj/use'

	#copy and rename imgs to use dir
	move_img(DIR, USE_DIR)

	#return isbn number from images
	ISBN = []

	for image in os.listdir(USE_DIR):
		img = f'{USE_DIR}/{image}'
		try:
			ISBN.append(img_decode(img))
		except Exception:
			print('decodingError')
			pass

	with open('isbns.txt', 'w') as f:
		for item in ISBN:
			f.write(item)
			f.write('\n')

	#send each isbn to isbn API and save the response (maybe filter it?)
	for id in ISBN:
		try:
			api_call = isbn_api(id)	
		except Exception:
			print('apiError')
			pass
		try:
			add_book(api_call)
		except Exception:
			print('insertError')
			pass

if __name__ == '__main__':
	main()
