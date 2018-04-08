import re
import os

from io import open
from setuptools import setup, find_packages

def get_version():
    init_py = open(os.path.join('src', 'risk_managed', '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

def get_requirements(f):
    return open(os.path.join('requirements', f)).read().splitlines()

try:
    from pypandoc import convert_file

    def read_md(f):
        return convert_file(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")

    def read_md(f):
        return open(f, 'r', encoding='utf-8').read()

setup(
    name='risk_managed',
    version=get_version(),
    author='Joshua Taylor Eppinette',
    author_email='josheppinette@icloud.com',
    url='https://github.com/jteppinette/risk-managed',
    description='an event management system for Universities and Greek Life organizations',
    long_description=read_md('README.md'),
    license='BSD',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'console_scripts': ['risk_managed=risk_managed:main']
    },
    install_requires=get_requirements('app.txt')
)
