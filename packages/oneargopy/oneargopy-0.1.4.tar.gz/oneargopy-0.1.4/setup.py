from setuptools import setup, find_packages

setup(
    name="oneargopy",
    version="0.1.3",
    author="Savannah Stephenson and Hartmut Frenzel",
    author_email="hartmut.frenzel@noaa.gov",
    description="A package for downloading and analyzing data from the Argo GDAC",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
