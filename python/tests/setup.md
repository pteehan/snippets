

    sudo pip install tox
    sudo apt-get install python-pytest

- Add tox.ini to root folder
- Add tests/test_foo.py
- In each py file add functions:

    def test_foo():
         assert 1 == 1

- Run from command line:

    tox

Or (quicker, no virtualenvs)

    PYTHONPATH=. py.test
