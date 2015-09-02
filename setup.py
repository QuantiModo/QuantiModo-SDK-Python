# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_client"
VERSION = "1.0.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="QuantiModo",
    author_email="",
    url="",
    keywords=["Swagger", "QuantiModo"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    QuantiModo makes it easy to retrieve normalized user data from a wide array of devices and applications.\n[Learn about QuantiModo](https://app.quantimo.do) or contact us at [help.quantimo.do](https://help.quantimo.do).\n\n Create an account at [QuantiModo](https://app.quantimo.do), sign in, and add\n\nsome data at https://app.quantimo.do/connect to try out the API for yourself.  As long as you&#39;re signed in, it will use your browser&#39;s cookie for authentication.  However, client applications must use OAuth2 tokens to access the API.
    """
)


