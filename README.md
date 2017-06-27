# MyProject

## Install

Make sure you have installed virtualenv and have the `virtualenv` command in
your `PATH`. On macOS you can do this with [brew](https://brew.sh/) and
`pyenv-virtualenv`. On most linux systems with Python, `virtualenv` is already
installed, but look for `python-virtualenv` otherwise.

```
virtualenv -p $(which python3) .env
.env/bin/pip install -r requirements.txt
.env/bin/python setup.py develop
```

The directory is named `.env` with a `.` at the front so that it is treated as
a hidden folder in UNIX systems.

To avoid having to keep typing `.env/bin` in front of commands, you can
activate your environment (modify certain environment variables like `PATH`)
like this:

```
source .env/bin/activate
```

And to deactivate it:

```
deactivate
```

The rest of the commands in this guide will assume you are running in an
activated Python virtual environment.

## Test

You can run the tests in an activated Python virtual environment like this:

```
nostetests
```
