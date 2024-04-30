import mysql.connector

#list_val should be a dict

def data_to_db(list_val):

#connect with mysql database
	
	mydb = mysql.connector.connect(
	  host="localhost",
	  password="hell",
	  user='root',
	  database="bookshelf",
	  port=3306
	)
	
	mycursor = mydb.cursor()

#values to be inserted into database
	cols = ['isbn','title','subtitle','authors','publisher','year','page_count']

	val =  {'isbn': '',
			'title': '',
			'subtitle': '',
			'authors': '',
			'publisher': '',
			'year': '',
			'pages': '0'}


#create a dict with wanted data from list_val AND split authors into two columns then removing it

	for field in cols:
		if field == 'authors':
			val['first_author'], *val['other_authors'] = list_val['authors']
			val['other_authors'] = str(val['other_authors']).replace('[', '').replace(']', '')
		if field in list_val.keys():
			val[field]=list_val[field]
	del val['authors']
	
#SQL commands for inserting data into books table
	sql = ("INSERT INTO books "
              "(isbn, title, subtitle, first_author,\
				  other_authors, publisher, year, pages) "
              "VALUES (%(isbn)s, %(title)s, %(subtitle)s, %(first_author)s,\
				  %(other_authors)s, %(publisher)s, %(year)s, %(pages)s)")
	
	

	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")



