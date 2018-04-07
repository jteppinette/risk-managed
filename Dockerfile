FROM tiangolo/uwsgi-nginx

ENV DEBUG False

COPY nginx.conf /etc/nginx/conf.d/
COPY uwsgi.conf /etc/uwsgi/uwsgi.ini

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

CMD /usr/bin/supervisord
