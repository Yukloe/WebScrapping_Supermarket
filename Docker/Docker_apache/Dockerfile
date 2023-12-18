FROM debian

RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get install -y libapache2-mod-php8.2 && \
    apt-get install -y php-mysql



# Ajout du nom dans le fichier de configuration d'Apache:
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

EXPOSE 80

RUN rm /var/www/html/index.html

COPY ./Docker_apache/html/index.php /var/www/html/index.php

ENTRYPOINT [ "/usr/sbin/apache2ctl", "-D", "FOREGROUND" ]