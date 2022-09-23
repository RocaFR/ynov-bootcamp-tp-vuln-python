FROM ubuntu:22.04

RUN apt update \
&& apt install wget -yq \
&& apt install gcc -yq \
&& apt install python3 -yq \
&& apt install python3-pip -yq \
&& pip3 install flask \
&& apt clean -y

ADD ./topsix /app
WORKDIR /app

RUN mkdir uploads \
&& chown -R www-data:www-data .

USER www-data

EXPOSE 5000

CMD bash -c "flask run -h 0.0.0.0"