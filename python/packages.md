reating packages

do this:

    package_name/
        __init__.py
        setup.py
        module_name/
             __init.__py
            myfile.py

then:
    from package_name.module_name import ClassInMyFile

more advanced:
    pkg/
    __init__.py
    setup.py
       pkg/
           __init.py__
           folder1/
             __init__.py
              file1.py

then in pkg/pkg/__init__.py:
    from pkg.folder1.file1.py import Class

Usage:
    from pkg Import Class
or
    import pkg
    pkg.Class()

To make the package installable:
    http://python-packaging-user-guide.readthedocs.io/distributing/#requirements-for-packaging-and-distributing

- add README.rst or README.md
- add setup.cfg if needed
- add MANIFEST.in if needed (to include additional files)
- add setup.py -- see sample [here](https://github.com/pypa/sampleproject/blob/master/setup.py)


To install:

    http://python-packaging-user-guide.readthedocs.io/installing/

    pip install -e path
(that makes it editable from source)

Use __init__.py to expose objects so they are easier to import

