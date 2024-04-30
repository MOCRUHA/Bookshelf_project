docker run --name bookshelfdb -e MYSQL_ROOT_PASSWORD=hell -e MYSQL_DATABASE=bookshelf -e MYSQL_USER=admin -d mysql

docker run -it --network bookshelfdb --rm mysql mysql -h bookshelf admin -p

