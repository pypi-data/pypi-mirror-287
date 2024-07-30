from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='pygfdrivers',
    version='0.1',
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown"
)
