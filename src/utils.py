import os
import shutil

from pyzbar.pyzbar import decode
import requests as req
import mysql.connector
import cv2


#--------------------------------------------------------------------------------------------
def isbn_api(isbn):

#api request for isbn
	resp = req.get(f'https://brasilapi.com.br/api/isbn/v1/{isbn}')

#request status code
	st_code = resp.status_code
	print('STATUS_CODE: ', st_code)

	return resp.json()

#--------------------------------------------------------------------------------------------
#list_val should be a dict
def add_book(list_val):

#connect with mysql database	
	cnx = mysql.connector.connect(
	  host='localhost',
	  password="hell",
	  user='root',
	  database="bookshelfdb",
	  port=3306
	)
#connection status message
	if (cnx.is_connected()):
		print("Connected")
	else:
		print("Not connected")

	cursor = cnx.cursor()

#attributes to be inserted into database
	cols = ['isbn','title','subtitle','authors','publisher','year','page_count']


#create a dict with wanted data from list_val AND join authors into one column
	val =  {}
	
	for field in cols:
		val[field] = list_val.get(f'{field}')

	val['authors'] = ','.join(map(str, val['authors']))

#SQL commands for inserting data into books table
	add = ("INSERT INTO books"
              "(isbn, title, subtitle, authors, publisher, year, page_count)"
              "VALUES (%(isbn)s, %(title)s, %(subtitle)s, %(authors)s, %(publisher)s, %(year)s, %(page_count)s)")

	cursor.execute(add, val)

	cnx.commit()
	print(cursor.rowcount, "record inserted.")
	cursor.close()
	cnx.close()

#--------------------------------------------------------------------------------------------
#pyzbar(decode) reads barcode and returns isbn
def img_decode(path):

    dec = decode(cv2.imread(f'{path}'))

    return (dec[0].data.decode())

#--------------------------------------------------------------------------------------------
#move images from storage dir to work dir
def move_img(src, dst):	
	#list all images
	imlist = os.listdir(src)

#rename and move one image at a time to the destination dir
	num=0
	for image in imlist:
		src_path = os.path.join(src, f'{image}')
		dst_path = os.path.join(dst, f'bc_{num}.jpg')
		shutil.copy(src_path, dst_path)
		num+=1

#--------------------------------------------------------------------------------------------