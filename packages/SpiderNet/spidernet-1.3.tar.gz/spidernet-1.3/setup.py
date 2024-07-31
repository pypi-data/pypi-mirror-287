from setuptools import setup, find_packages

VERSION = '1.3'
DESCRIPTION = 'A python package to simplify web scraping . Built using REgex and Curl'
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SpiderNet",
    version="1.3",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vishal",
    author_email="vishalvenkat2604@gmail.com",
    license='MIT',
    packages=find_packages(),
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
    url="https://github.com/query-lang/SpiderWeb"
   
)