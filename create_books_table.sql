USE bookshelfdb;

CREATE TABLE books(
	isbn VARCHAR(20) NOT NULL,
	title VARCHAR(255) NOT NULL,
	subtitle VARCHAR(255),
	authors VARCHAR(255),
	publisher VARCHAR(255),
	year INT,
	page_count INT,
	PRIMARY KEY (isbn)
);


-- INSERT INTO books(isbn, title) VALUES (1211234, 'gjesus');

