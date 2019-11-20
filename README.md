# cythonize-setuptools
Cythonize python codes and build wheel distribution package to hide your python codes.

Cythonized wheel package will only distribute shared libraries (.so) which provide proper protection for your codes.



Usage:
   1. Fill in proper PKG_NAME, PKG_VERSION etc. in setup.py
   2. For cythonize packaging: CYTHONIZE=1 python setup.py bdist_wheel
   3. For normal packaging: python setup.py bdist_wheel

Reference:
https://bucharjan.cz/blog/using-cython-to-protect-a-python-codebase.html
