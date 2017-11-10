testing

You can use unittest, py.test, or nose.

py.test looks nicest for sure.
Also use tox to automate.

pip install tox

Creata a file called tox.ini, in same dir as setup.py, with these contents:
    [tox]
    envlist = py26, py27 # this will test aganst python 2.6 and 2.7
    [testenv]
    deps = pytest # install pytest in the venvs
    commands = py.test

set up a directory in the package top level called tests/
name files test_foo.py (not testFoo.py)

Then run ['tox'](https://tox.readthedocs.io/en/latest/)

Alternatively just run py.test, but you won't get the benefits of virtualenvs

- make sure that “mypkg” is importable, for example by typing once:
- pip install -e .  # install package using setup.py in editable mode


If you get this error:

    close failed in file object destructor:
    sys.excepthook is missing
    lost sys.stderr


Try wrapping the test code in this:

    import sys
    (...)
    sys.stdout.flush()


