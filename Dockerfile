FROM ubuntu:22.04

RUN apt update \
&& apt install python3 -yq \
&& apt install python3-pip -yq \
&& apt clean -y \
&& pip3 install flask

ADD ./ynov-bootcamp-tp-vuln-python/ /chall
WORKDIR /chall

RUN chown -R www-data:www-data .

USER www-data

EXPOSE 5000

CMD bash -c "source start_app.sh"