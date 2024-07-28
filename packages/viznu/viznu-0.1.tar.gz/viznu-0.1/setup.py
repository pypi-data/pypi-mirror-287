# setup.py

from setuptools import setup, find_packages

setup(
    name='viznu',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
    ],
    author='Apekshik Panigrahi',
    author_email='apekshik@gmail.com',
    description='A simple and intuitive library for data visualization and preprocessing for ML and DL applications',
    url='https://github.com/yourusername/viznu',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)