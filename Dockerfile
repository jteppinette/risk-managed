FROM python:2.7

ENV DEBUG False

EXPOSE 80

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir .

ENTRYPOINT ["risk_managed"]
CMD ["rungunicorn", "-b", "0.0.0.0:80"]
