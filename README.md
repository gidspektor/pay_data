## Development environment setup

# To run with pipenv do the below

### PyEnv installation and setup

This project uses Python version **3.7.2**.

Using the [PyEnv](https://github.com/pyenv/pyenv) to manage Python versions is recommended. Installation instructions can be found at the provided link.

The [PyEnv](https://github.com/pyenv/pyenv) tool might require the [zlib](https://www.zlib.net/) libaries to be install on your local operating system in order to build the requested versions Python. Use the package manager of your choice to install it.

### Installing project dependecies

Use the following command to install the project dependencies:

```
$ pipenv install
```

### Running a development instance of the service

Use the following command to run a development instance of the service:

```
$ pipenv run python run.py
```

Go to localhost:5000/2015_open_payment

# To run without pipenv

Install the following dependencies:
```
flask 1.1.1
```
```
pytest 4.3.1
```
```
pandas *
```
```
xlwt *
```

```
$ python run.py
```
Go to localhost:5000/2015_open_payment

### Running tests

Use the following command to run the tests for the service:

With pipenv:
```
$ pipenv run pytest
```

Without pipenv:
```
$ pytest
```