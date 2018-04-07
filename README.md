# Risk Managed - *an event management system for Universities and Greek Life organizations*

## Development

### Required Software

* [docker](https://docs.docker.com/)
* [git](https://git-scm.com/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)

### Getting Started

```
$ git clone https://github.com/jteppinette/risk-managed.git && cd risk-managed
$ virtualenv venv
$ venv/bin/pip install -e .
$ docker-compose up -d db minio mail
$ venv/bin/risk_managed makemigrations
$ venv/bin/risk_managed migrate
$ venv/bin/risk_managed createfixturedata -f
$ venv/bin/risk_managed runserver
```

## Usage

### Environment Variables

* DEBUG           `default: True`
* DB_NAME         `default: db`
* DB_USER         `default: db`
* DB_PASSWORD     `defualt: secret`
* DB_HOST         `default: 0.0.0.0`
* DB_PORT         `default: 5432`
* MINIO_ACCESSKEY `default: access-key`
* MINIO_BUCKET    `default: test`
* MINIO_SERVER    `default: 0.0.0.0:9000`
* MINIO_SECURE    `default: false`
* MINIO_SECRET    `default: secret-key`
* SESSION_SECRET  `defualt: secret`
* MAIL_FROM       `default: notifications@risk-managed.localhost`
* MAIL_HOST       `default: 0.0.0.0`
* MAIL_PORT       `default: 1025`
* MAIL_PASSWORD   `default: `
* MAIL_USER       `default: `
* MAIL_USE_TLS    `default: False`
* MAIL_USE_SSL    `default: False`
