from setuptools import setup

setup(
    name='sdnv',
    version='0.1.0',
    description='Module to provide encoding/decoding of RFC6256 SDNV',
    long_description=open('README.rst').read(),
    author='Marco \'don\' Kaulea',
    author_email='donmarco42@gmail.com',
    url='https://github.com/Don42/sdnv',
    packages=['sdnv'],
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
