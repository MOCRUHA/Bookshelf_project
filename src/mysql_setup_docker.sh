#!/bin/bash

docker run  --name bookshelf_db -e MYSQL_ROOT_PASSWORD=hell  -p 3306:3306 -d mysql

docker exec -it bookshelf_db bash
