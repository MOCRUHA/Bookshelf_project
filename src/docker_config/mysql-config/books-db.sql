USE bookshelf;

CREATE TABLE books(
	isbn VARCHAR(20) NOT NULL,
	title VARCHAR(255) NOT NULL,
	subtitle VARCHAR(255),
	pages INT,
	year INT,
	publisher VARCHAR(255),
	author1 VARCHAR(255),
	author2 VARCHAR(255),
	author3 VARCHAR(255),
	author4 VARCHAR(255),
	PRIMARY KEY (isbn)

);

