FROM python:3.7.4-slim

WORKDIR /usr/src/app

RUN apt-get update -y && \
    apt-get install libpq-dev libjpeg-dev libtiff5-dev -y

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DEVELOPMENT False

EXPOSE 80

RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "risk_managed.wsgi", "-b", "0.0.0.0:80", "--log-file", "-"]
