
import os
import streamlit as st
import mysql.connector
import pandas as pd

#query database books
def qry_books():
	
#connect with mysql database
    try:
        cnx = mysql.connector.connect(
            host='192.168.15.162',
            password="hell",
            user='root',
            database="bookshelfdb",
            port=3306
        )

        query = ('SELECT * FROM books')

        query_books = pd.read_sql(query, cnx)

        st.table(query_books)

    except Exception as e:
        cnx.close()
        print(str(e))
    
    
    
if __name__ == '__main__':
    qry_books()
