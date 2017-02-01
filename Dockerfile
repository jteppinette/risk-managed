FROM tiangolo/uwsgi-nginx

ENV DEBUG False

COPY nginx.conf /etc/nginx/conf.d/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

CMD /usr/bin/supervisord
