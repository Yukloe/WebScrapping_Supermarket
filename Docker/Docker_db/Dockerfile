#Image MySQL

FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./Docker_db/init.sql /docker-entrypoint-initdb.d/
COPY ./Docker_db/list_product.csv /docker-entrypoint-initdb.d/