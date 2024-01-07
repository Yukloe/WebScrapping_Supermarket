#Image MySQL

FROM mysql:5.7.43

ENV MYSQL_ROOT_PASSWORD=root

COPY ./Docker_db/init.sql /docker-entrypoint-initdb.d/
COPY ./Docker_db/list_product.csv /docker-entrypoint-initdb.d/