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

REQUIRES = []

setup(
    name="SwaggerPetstore",
    version="1.0.0",
    description="QuantiModo",
    author_email="info@interactuamovil.com",
    url="",
    keywords=["Swagger", "QuantiModo"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    QuantiModo makes it easy to retrieve normalized user data from a wide array of devices and applications.\n\n[Learn about QuantiModo](https://quantimo.do) or contact us at [help.quantimo.do](https://help.quantimo.do).\n\n Contact info@quantimo.do for an api key to test the authorization filters.\n * Test User Name: `user`\n * Password: `SuperPassword123!!!`
    """
)


