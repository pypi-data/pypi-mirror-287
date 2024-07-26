from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name="pygeolang",
  version="0.3.1",
  author="Priyanshu Sharma",
  author_email="sharma.priyanshu96@gmail.com",
  description="A Python package for accessing country, continent, and language data.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/ipriyaaanshu/pygeolang",
  packages=find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  install_requires=[
    "pycountry",
    "langcodes"
  ],
  package_data={'pygeolang': ['dataset.pickle']},
  include_package_data=True,
)