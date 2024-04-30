from flask import Flask
import mysql.connector

import books_query

app = Flask(__name__)

@app.route('/')

# def print_query(query):
#     query = str(query)
#     return(f"<p> {{query}} </p>")

# q = books_query.query_books()

def prints():
    return f'| Título: coco | Subtítulo: bambu | Editora: novatec |'
prints()