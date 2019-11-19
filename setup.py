"""Setup script.
   Usage:
   1. For cythonize packaging: CYTHONIZE=1 python setup.py bdist_wheel
   2. For normal packaging: python setup.py bdist_wheel

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from setuptools import find_packages
from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools.dist import Distribution

PKG_NAME = ''
PKG_VERSION = ''
PKG_AUTHOR = ''
PKG_URL = ''
REQUIRED_PACKAGES = ['']
PACKAGES = find_packages(exclude=['.*test'])
PACKAGE_DATA = {'': ['*.so']}
SRC = ''

KEYWORDS = ()
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.6',
    'Operating System :: POSIX :: Linux',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries']
LICENSE = 'Apache 2.0'

class BinaryDistribution(Distribution):
  def has_ext_modules(self):
    return True

if os.environ.get('CYTHONIZE') == '1':
    setup(
        name=PKG_NAME,
        version=PKG_VERSION,
        author=PKG_AUTHOR,
        url=PKG_URL,
        install_requires=REQUIRED_PACKAGES,
        packages=[],
        include_package_data=True,
        package_data=PACKAGE_DATA,
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS,
        license=LICENSE,
        ext_modules=cythonize([Extension(SRC + '.*', [SRC + '/*.py'])]),
        build_dir="build",
        compiler_directives=dict(
            always_allow_keywords=True
        ),
        cmdclass=dict(
            build_ext=build_ext
        ),
    )
else:
    setup(
        name=PKG_NAME,
        version=PKG_VERSION,
        author=PKG_AUTHOR,
        url=PKG_URL,
        install_requires=REQUIRED_PACKAGES,
        packages=PACKAGES,
        distclass=BinaryDistribution,
        zip_safe=False,
        include_package_data=True,
        package_data=PACKAGE_DATA,
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS,
        license=LICENSE)
