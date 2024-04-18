

def data_to_db(list_val):

	import mysql.connector
	
	mydb = mysql.connector.connect(
	  host="localhost",
	  password="hell",
	  user='batata',
	  database="bookshelf"
	)
	 
	mycursor = mydb.cursor()
	 
	sql = "INSERT INTO books (isbn,\
							 title,\
							 subtitle,\
							 authors,\
							 publisher,\
							 year,\
							 page_count\
							 ) VALUES (%s, %s, %s, %s, %s, %s, %s)"


	print(list_val)
	val = tuple(list_val)
	print(val)
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")