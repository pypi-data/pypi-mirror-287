from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# Setting up
setup(
    name="time_calcfreename",
    version="0.0.3",
    author="Someone",
    author_email="<mail@neuralnine.com>",
    description="Hi Mai",
    long_description_content_type="text/markdown",
    long_description="This python package contains a single function that calculates the exact time after a specified number of seconds have passed",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
