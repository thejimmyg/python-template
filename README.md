# MyProject

## Install

```
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python setup.py develop
cd doc
```

Rename `myproject` to your project name.

Setup docs:

```
sphinx-quickstart
```

## Test

You can run the tests in an activated Python virtual environment like this:

```
venv/bin/pytest test/*.py
```


## Run

You must run the example from the virtual environment you created. You can do so like this:

```
venv/bin/python -m myproject
```

## Develop

Make sure tests pass and files comply with PEP8:

```
venv/bin/pytest
venv/bin/autopep8
```

Make sure the `CHANGELOG.rst`, `LICENSE.rst` and `AUTHORS.rst` files are up to
date and that you've set the correct version number in `setup.py` and
`docs/conf.py`.

Put dev dependencies into `requirements.txt` and runtime dependencies into `setup.py`.

Make the documentation like this:

```
cd docs
. ../venv/bin/activate
make html
deactivate
```

Test with coverage:

```
venv/bin/pytest --cov=myproject test/*.py
```

Upload to pypi with:

```
venv/bin/python setup.py sdist
venv/bin/python setup.py upload
```

The HTML files you've built are included in the distribution thanks to the contents of `MANIFEST.in`. XXX

Can now upload to readthedocs. XXX

Can upload to github with coverage.io

Check coverage. XXX

Check build passes XXX
