# Risk Managed - *an event management system for Universities and Greek Life organizations*

## Development

### Required Software

* [docker](https://docs.docker.com/)
* [git](https://git-scm.com/)
* [OpenSSL](https://www.openssl.org)

### Getting Started

```
$ git clone https://github.com/jteppinette/risk-managed.git && cd risk-managed
$ echo "127.0.0.1 storage" | sudo tee -a /etc/hosts
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ docker-compose up -d db mail storage
$ python manage.py migrate
$ python manage.py runserver
```

## Usage

### Environment Variables

```
DEVELOPMENT                default: True
DATABASE_URL               default: postgres://db:secret@0.0.0.0:5432/db
SECRET_KEY                 default: secret
SMTP_DOMAIN                default: risk-managed.localhost
SMTP_SERVER                default: 0.0.0.0
SMTP_PORT                  default: 1025
SMTP_PASSWORD
SMTP_LOGIN
STORAGE_ACCESS_KEY_ID      default: access-key-id
STORAGE_SECRET_ACCESS_KEY  default: secret-access-key
STORAGE_BUCKET             default: storage
STORAGE_URL                default: http://0.0.0.0:9000
```

## Deployment

### Heroku

```
$ heroku create
$ heroku addons:create mailgun:starter
$ heroku addons:create bucketeer:hobbyist
$ heroku config:set SECRET_KEY=`openssl rand -base64 50`
$ heroku config:set DEVELOPMENT=False
$ git push heroku master
```
