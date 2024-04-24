FROM mysql

WORKDIR /db

# ENV MYSQL_ROOT_PASSWORD 1234
# ENV MYSQL_USER 'brachya'
# ENV MYSQL_PASSWORD: '1234'

COPY ./mysqlsampledatabase.sql /docker-entrypoint-initdb.d
