

def data_to_db(list_val):

	import mysql.connector
	
	mydb = mysql.connector.connect(
	  host="localhost",
	  password="hell",
	  user='root',
	  database="bookshelf"
	)
	
	mycursor = mydb.cursor()


	list_val['first_author'], *list_val['other_authors'] = list_val['authors']
	list_val['other_authors'] = str(list_val['other_authors']).replace('[', '').replace(']', '0')
	

	cols = ['isbn','title','subtitle','first_author', 'other_authors','publisher','year','page_count']

	for field in cols:
		if field not in list_val.keys():
			list_val[field]='0'

	print(list_val)

	vals = ', '.join(['%('+ str(list_val[item]) +')s' for item in cols])
	

	sql = f"INSERT INTO books ({cols}) VALUES ({vals})"

	print('-------------------')
	print(type(vals))
	print('-------------------')

	print('AAAAAAAA')
	print(cols)
	

	vals = vals.split(', ')

	print('BBBBBBBB')
	print(vals)

	mycursor.execute(sql, vals)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")