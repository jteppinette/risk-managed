# Risk Managed - *an event management system for Universities and Greek Life organizations*

## Initialize Environment

1. Install `pip` and `virtualenv`

2. `git clone https://github.com/jteppinette/risk-managed.git`

3. `virtualenv rm`

4. `source rm/bin/activate`

5. Run a mysql server. The default required settings can be found in `project/settings.py`. A compatible docker container would look like:
    * `docker run -p 3306:3306 -d -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=risk-managed -e MYSQL_USER=risk-managed -e MY_SQL_PASSWORD=secret --name mysql mysql`

6. `python manage.py createsuperuser` - _Create a user by following the Django *createsuperuser* command prompts. This superuser will be used to create companies and administor the system._

7. Visit `http://localhost:8000/admin`

8. Create new Universities and Organziations that can be used to register with.

9. Visit `http://localhost:8000/`

10. Register a new host or administrator and login.

## Settings

There are many settings and features that are configurable in the _/<root>/project/settings.py_ file.
Some of which are also made available through environment variables.
Read through this file for detailed documentation regarding each available setting, or
view the online [Django v1.10 Documentation](https://docs.djangoproject.com/en/1.10/ref/settings/).

## Docker

1. `docker build . -t amp`

2. `docker run -p 3306:3306 -d \
      -e MYSQL_DATABASE=<db name> \
      -e MYSQL_USER=<db user> \
      -e MYSQL_PASSWORD=<db password> \
      -e MYSQL_ROOT_PASSWORD=<db password> \
      --name mysql mysql`

3. `docker run -it -p 8080:80 \
      -e SECRET_KEY=<secret> \
      -e DB_NAME=<db name> \
      -e DB_USER=<db user> \
      -e DB_PASSWORD=<db password> \
      -e DB_HOST=<db host> \
      -e DB_PORT=<db port> \
      --rm --name risk-managed risk-managed`

4. `docker exec -it amp python manage.py migrate`

5. `docker exec -it amp python manage.py createsuperuser`


### Debug

In a producton environment, be sure to set the *DEBUG* configuration item to _False_. This will disable the automatic wen interface error reporting and expensive debugging routines.
