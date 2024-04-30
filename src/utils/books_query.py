import mysql.connector


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
        
