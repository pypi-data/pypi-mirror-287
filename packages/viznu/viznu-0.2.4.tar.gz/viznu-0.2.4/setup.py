# setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as f: 
    description = f.read() 

setup(
    name='viznu',
    version='0.2.4',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
    ],
    author='Apekshik Panigrahi',
    author_email='apekshik@gmail.com',
    url='https://github.com/apekshik/viznu',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)