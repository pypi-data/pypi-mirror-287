# my_simple_package/setup.py

from setuptools import find_packages, setup

setup(
    name='gee_package',
    version='0.1',
    packages=find_packages(),
    description='A simple arithmetic operations package',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
