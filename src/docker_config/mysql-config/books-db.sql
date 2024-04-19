USE bookshelf;

CREATE TABLE books(
	isbn VARCHAR(20) NOT NULL,
	title VARCHAR(255) NOT NULL,
	subtitle VARCHAR(255),
	pages INT,
	year INT,
	publisher VARCHAR(255),
	author VARCHAR(255),
	PRIMARY KEY (isbn)

);
