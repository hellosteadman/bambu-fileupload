# Bambu FileUpload

A wrapper around the
[jQuery.fileupload](http://blueimp.github.io/jQuery-File-Upload/) library

## About Bambu Bootstrap

Todo

## About Bambu Tools 2.0

This is part of a toolset called Bambu Tools. It's being moved from a namespace
of `bambu` to its own 'root-level' package, along with all the other tools in
the set. If you're upgrading from a version prior to 2.0, please make sure to
update your code to use `bambu_fileupload` rather than `bambu.fileupload`.

## Installation

Install the package via Pip:

```
pip install bambu-fileupload
```

Add it to your `INSTALLED_APPS` list and add the necessary front-end libraries
to your `BOWER_INSTALLED_APPS` list (see the
[django-bower documentation](http://django-bower.readthedocs.org/en/latest/))
for details on managing static files through Bower.

```python
INSTALLED_APPS = (
    ...
    'djangobower',
)

BOWER_INSTALLED_APPS = (
    ...
    'jquery-hashchange',
	'jquery-file-upload',
	'jquery.iframe-transport'
)
```

Remember to run `python manage.py bower install`,
`python manage.py collectstatic` and `python manage.py migrate` (or `syncdb`).

## Basic usage

Todo

## Documentation

Todo

## Questions or suggestions?

Find me on Twitter (@[iamsteadman](https://twitter.com/iamsteadman))
or [visit my blog](http://steadman.io/).
