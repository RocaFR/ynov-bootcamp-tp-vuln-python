FROM python:3.7.14-slim-bullseye

RUN apt-get update -y \
        && apt-get install -y python3-pip python3-dev build-essential sudo libpq-dev \
        && apt install file -y

RUN usermod -d /home/app www-data

WORKDIR /home/app
COPY ./front/requirements .

RUN pip install --upgrade pip \
        && pip install -r requirements

COPY ./front/python .

RUN chmod -r /tmp /var/tmp

RUN chmod 755 -R /home/app/uploads

RUN chown -R www-data:www-data .

USER www-data

CMD ["gunicorn","-b","0.0.0.0:1337","--workers=5","app:app","--reload"]