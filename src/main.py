import os
import shutil

from pyzbar.pyzbar import decode
import requests as req
import mysql.connector
import cv2


#--------------------------------------------------------------------------------------------
def isbn_api_call(isbn):

#api request for isbn
	resp = req.get(f'https://brasilapi.com.br/api/isbn/v1/{isbn}')

#request status code
	st_code = resp.status_code
	print(st_code)

	return resp.json()

#--------------------------------------------------------------------------------------------
def query_books():
    cnx = mysql.connector.connect(host="localhost",
                                        password="hell",
                                        user='root',
                                        database="bookshelf",
                                        port=3306)

    cursor = cnx.cursor()

    stats = ("SELECT count(isbn) as qtd FROM books")

    cursor.execute(stats)

    for qtd in cursor:
        qtd = str(qtd).replace(',', '')
        quant = f"Quantidade de livros: {qtd}"

    query = ("SELECT title, subtitle, publisher FROM books")

    cursor.execute(query)

    for (title, subtitle, publisher) in cursor:
        sql = f'| Título: {title} | Subtítulo: {subtitle} | Editora: {publisher} |'
    return quant, sql

    cursor.close()
    cnx.close()

#--------------------------------------------------------------------------------------------
#list_val should be a dict
def data_to_db(list_val):

#connect with mysql database
	
	cnx = mysql.connector.connect(
	  host='192.168.15.162',
	  password="hell",
	  user='root',
	  database="bookshelfdb",
	  port=3306
	)
	
	print(list_val)	
	if (cnx.is_connected()):
		print("Connected")
	else:
		print("Not connected")

	cursor = cnx.cursor()

#values to be inserted into database
	cols = ['isbn','title','subtitle','authors','publisher','year','page_count']


#create a dict with wanted data from list_val AND split authors into two columns then removing it
	val =  {}
	

	for field in cols:
		val[field] = list_val.get(f'{field}')

	val['authors'] = ','.join(map(str, val['authors']))

#SQL commands for inserting data into books table
	add = ("INSERT INTO books"
              "(isbn, title, subtitle, authors, publisher, year, page_count)"
              "VALUES (%(isbn)s, %(title)s, %(subtitle)s, %(authors)s, %(publisher)s, %(year)s, %(page_count)s)")
	
	print('!!!!!!!!!!!!!!', val)

	cursor.execute(add, val)

	cnx.commit()
	print(cursor.rowcount, "record inserted.")
	cursor.close()
	cnx.close()


#--------------------------------------------------------------------------------------------
def img_to_code(path):

    dec = decode(cv2.imread(f'{path}'))

    return (dec[0].data.decode())
    

#--------------------------------------------------------------------------------------------
#move images from storage dir to work dir
def move_img(src, dst):	
	#list all images
	imlist = os.listdir(src)

	#rename and move one image at a time to the dst dir
	num=0
	for image in imlist:
		src_path = os.path.join(src, f'{image}')
		dst_path = os.path.join(dst, f'bc_{num}.jpg')
		shutil.copy(src_path, dst_path)
		num+=1

#--------------------------------------------------------------------------------------------
def main():
	#dir where imgs are kept
	DIR = r'/home/gusta/Dropbox/mobile_imgs'
	USE_DIR = r'/home/gusta/Desktop/pj/use'

	#copy and rename imgs to use dir
	move_img(DIR, USE_DIR)

	#return isbn number from images
	ISBN = []

	for image in os.listdir(USE_DIR):
		img = f'{USE_DIR}/{image}'
		try:
			ISBN.append(img_to_code(img))
		except Exception:
			print('decodingError')
			pass

	with open('isbns.txt', 'w') as f:
		for item in ISBN:
			f.write(item)
			f.write('\n')

	#send each isbn to isbn API and save the response (maybe filter it?)
	for id in ISBN:
#	try:
		print(id)
		api_call = isbn_api_call(id)
		
#	except Exception:
#		print('apiError')
#		pass
#		try:
			#print('------', api_call)
		data_to_db(api_call)
#		except Exception:
		print('injectError')
#			pass

if __name__ == '__main__':
	main()
