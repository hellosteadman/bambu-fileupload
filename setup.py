#!/usr/bin/env python
from setuptools import setup
from os import path

setup(
    name = 'bambu-fileupload',
    version = '3.1',
    description = 'A wrapper around the jQuery.fileupload library',
    author = 'Steadman',
    author_email = 'mark@steadman.io',
    url = 'http://pypi.python.org/pypi/bambu-fileupload',
    install_requires = [
        'Django>=1.8'
        'django-bower'
    ],
    packages = [
        'bambu_fileupload',
        'bambu_fileupload.migrations',
        'bambu_fileupload.templatetags',
    ],
    package_data = {
        'bambu_fileupload': [
            'static/fileupload/css/*.css',
            'static/fileupload/img/*.gif',
            'static/fileupload/img/filetypes/*.png',
            'static/fileupload/js/*.js',
            'templates/fileupload/*.html'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django'
    ]
)
