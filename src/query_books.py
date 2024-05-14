

import streamlit
import mysql.connector

#query database books
def qry_books():
	
#connect with mysql database	
    cnx = mysql.connector.connect(
	  host='192.168.15.162',
	  password="hell",
	  user='root',
	  database="bookshelfdb",
	  port=3306
	)
	
    cursor = cnx.cursor()

#connection status message
    if (cnx.is_connected()):
        print("Connected")
    else:
        print("Not connected")

    query = ('SELECT * FROM books')

    cursor.execute(query)
    cursor.close()
    cnx.close()