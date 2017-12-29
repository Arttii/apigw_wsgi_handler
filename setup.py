# Copyright (c) 2010-2017 Benjamin Peterson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import with_statement

# apigw_wsgi_handler is a dependency of setuptools, so using setuptools creates a
# circular dependency when building a Python stack from source. We
# therefore allow falling back to distutils to install apigw_wsgi_handler.
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import apigw_wsgi_handler

apigw_wsgi_handler_classifiers = [
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

with open("README.rst", "r") as fp:
    apigw_wsgi_handler_long_description = fp.read()

setup(name="apigw_wsgi_handler",
      version=apigw_wsgi_handler.__version__,
      author="Artyom Topchyan",
      author_email="artyom.topchyan@live.com",
      url="http://pypi.python.org/pypi/apigw_wsgi_handler/",
      tests_require=["pytest"],
      install_requires=['werkzeug']
      py_modules=["apigw_wsgi_handler"],
      description="Python 2 and 3 compatibility utilities",
      long_description=apigw_wsgi_handler_long_description,
      license="MIT",
      classifiers=apigw_wsgi_handler_classifiers
      )
