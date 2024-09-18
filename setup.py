# setup.py

from setuptools import setup, find_packages

setup(
    name='mobius_linked_list',
    version='0.1.0',
    packages=find_packages(),
    description='A Python package implementing the Möbius Linked List data structure.',
    author='Moudather Chelbi',
    author_email='moudather.chelbi@gmail.com',
    url='https://github.com/vinerya/mobius_linked_list',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
