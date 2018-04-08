import os
import sys

from django.core.management import execute_from_command_line

__title__ = 'Risk Managed'
__version__ = '0.0.0'
__author__ = 'Joshua Taylor Eppinette'
__license__ = 'BSD'

VERSION = __version__

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "risk_managed.settings")
    execute_from_command_line(sys.argv)
