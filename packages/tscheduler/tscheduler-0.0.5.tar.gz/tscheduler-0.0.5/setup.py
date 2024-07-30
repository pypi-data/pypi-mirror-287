from setuptools import setup, find_packages
from os import path

working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tscheduler",
    author="The Taibaoui Mohammed",
    author_email="taibaoui.mohamed1988@gmail.com",
    description="task scheduler package",
    long_description=long_description,
    version="0.0.5",
    long_description_content_type="text/markdown",
    packages=["tscheduler"],
)
