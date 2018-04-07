from setuptools import setup, find_packages

setup(
    name='risk_managed',
    version='0.0.0',
    author='Joshua Taylor Eppinette',
    author_email='josheppinette@icloud.com',
    url='https://github.com/jteppinette/risk-managed',
    description='an event management system for Universities and Greek Life organizations',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'console_scripts': ['risk_managed=risk_managed:main']
    },
    install_requires=[
        'Django==1.10.5',
        'Pillow==4.0.0',
        'argparse==1.2.1',
        'pytz==2013.8',
        'psycopg2==2.7.1',
        'minio==2.2.1',
        'gunicorn==19.7.1'
    ]
)
