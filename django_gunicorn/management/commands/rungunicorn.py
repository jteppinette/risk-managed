from django.core.management.base import BaseCommand
from django.core.wsgi import get_wsgi_application

from gunicorn.six import iteritems

import multiprocessing
import gunicorn.app.base


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '-b',
            '--bind',
            dest='bind',
            type=str,
            default='0.0.0.0:8000',
            help='what tcp socket to bind to'
        )
        parser.add_argument(
            '-w',
            '--workers',
            dest='workers',
            type=int,
            default=(multiprocessing.cpu_count() * 2) + 1,
            help='how many workers to instantiate'
        )
        parser.add_argument(
            '-p',
            '--pid',
            dest='pidfile',
            type=str,
            help='a filename to use or the pid file'
        )
        parser.add_argument(
            '--log-file',
            '--error-logfile',
            dest='errorlog',
            type=str,
            default='-',
            help='a filename to write error logs'
        )
        parser.add_argument(
            '--access-logfile',
            dest='accesslog',
            type=str,
            default='-',
            help='a filename to write access logs'
        )

    def handle(self, *args, **kwargs):
        options = {
            'bind': kwargs.get('bind'),
            'workers': kwargs.get('workers'),
            'pidfile': kwargs.get('pidfile'),
            'errorlog': kwargs.get('errorlog'),
            'accesslog': kwargs.get('accesslog')
        }
        StandaloneApplication(get_wsgi_application(), options).run()


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        for key, value in iteritems(self.options):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
