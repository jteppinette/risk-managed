FROM python:2.7 as builder
WORKDIR /usr/src/app
RUN apt-get update -y && \
    apt-get install pandoc -y
COPY ./requirements ./requirements
RUN pip install --no-cache-dir -r requirements/app.txt && \
    pip install --no-cache-dir -r requirements/packaging.txt
COPY . .
RUN make build

FROM python:2.7-slim
RUN apt-get update -y && \
    apt-get install libpq-dev libjpeg-dev libtiff5-dev -y
COPY --from=builder /usr/src/app/target/risk_managed.pex /usr/local/bin/
ENV DEBUG False
EXPOSE 80
ENTRYPOINT ["risk_managed.pex"]
CMD ["rungunicorn", "-b", "0.0.0.0:80"]
