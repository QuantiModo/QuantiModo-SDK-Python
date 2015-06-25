import sys
from setuptools import setup, find_packages



# To install the library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed.
# Try reading the setuptools documentation:
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi"]

setup(
    name="SwaggerPetstore",
    version="1.0.0",
    description="QuantiModo",
    author_email="",
    url="",
    keywords=["Swagger", "QuantiModo"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    QuantiModo makes it easy to retrieve normalized user data from a wide array of devices and applications.\n\n[Learn about QuantiModo](https://quantimo.do) or contact us at [help.quantimo.do](https://help.quantimo.do).\n\n Create an account at [QuantiModo](https://quantimo.do), sign in, and add some data at https://quantimo.do/connect to try out the API for yourself.  As long as you&#39;re signed in, it will use your browser&#39;s cookie for authentication.  However, client applications must use OAuth2 tokens to access the API.
    """
)










