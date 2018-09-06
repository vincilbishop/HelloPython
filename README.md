# Hello Python!

## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run hellopython cli application

$ hellopython --help


### run pytest / coverage

$ make test
```


### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```
$ make dist

$ make dist-upload
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `HelloPython`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it hellopython --help
```

__________

![SurgeForward Logo](https://surgeforward.com//wp-content/themes/understrap-master/images/logo.png) 

Thanks to [Surge](https://www.surgeforward.com/) for their generous support of this and many other open source projects benefiting our community! 
