from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.1'
DESCRIPTION = 'Test package for OpenAI evaluation'
LONG_DESCRIPTION = 'A test package for demonstrating OpenAI package setup.'

# Setting up
setup(
    name="oaieval",
    version=VERSION,
    author="OpenAI",
    author_email="adam@openai.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['openai', 'evaluation', 'test'],
)
