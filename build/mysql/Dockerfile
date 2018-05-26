FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD P@ssword
ENV MYSQL_DATABASE mydb
ENV MYSQL_USER naresh
ENV MYSQL_PASSWORD P@ssword

COPY . /authorapp
ADD my.cnf /etc/mysql/my.cnf
