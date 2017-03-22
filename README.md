# Risk Managed - *an event management system for Universities and Greek Life organizations*

## Development

### Required Software

* [docker](https://docs.docker.com/)
* [git](https://git-scm.com/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)

### Getting Started

1. `git clone https://github.com/jteppinette/risk-managed.git`

2. `virtualenv venv`

3. `source venv/bin/activate`

4. `pip install -r requirements.txt`

5. `docker-compose up -d db`

6. `python manage.py migrate`

7. `python manage.py createfixturedata`

8. `python manage.py runserver`

## Usage

### Environment Variables

Any variables marked as `insecure: true` should be overriden before being added to a production system.

* DEBUG           `default: True`
* DB_NAME         `default: db`
* DB_USER         `default: db`
* DB_PASSWORD     `defualt: secret, insecure: true`
* DB_HOST         `default: 0.0.0.0`
* DB_PORT         `default: 5432`
* SESSION_SECRET  `defualt: secret, insecure: true`

### Docker

1. `docker build . -t app`

2. `docker run \
      -d
      -e POSTGRES_DB=db
      -e POSTGRES_USER=db
      -e POSTGRES_PASSWORD=db-secret
      --name db
      postgres:9.6`

3. `docker run
      -d
      -p 8000:80
      -e SESSION_SECRET=session-secret
      -e DB_NAME=db
      -e DB_USER=db
      -e DB_PORT=5432
      -e DB_PASSWORD=db-secret
      -e DB_HOST=db
      --link db
      --name app
      app`

4. `docker exec -it app python manage.py migrate`

5. `docker exec -it app python manage.py createfixturedata`
