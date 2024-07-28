from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'Indian Stock Data Featch and Represent Graphical Format '
LONG_DESCRIPTION = 'Featach difrant type of stock data, using nse baskend rest api. and create csv file and reprent graph format.'

# Setting up
setup(
    name="StockExchange",
    version=VERSION,
    author="Kaushal Zine",
    author_email="<kaushalzine.it@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python','scikit-learn', 'numpy', 'pandas', 'matplotlib','datetime','requests'],
    keywords=['python', 'nse', 'stock', 'sharemarket', 'Stock market', 'csv'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)