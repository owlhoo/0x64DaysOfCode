from setuptools import setup

# make virtualenv, source it into terminal then python setup.py install and you're donezo

setup(
    name='package_name',
    version='0.0001',
    description='THE description',
    url='localhost',
    install_requires=['patience'],

    packages=['some_pckg'],
)
