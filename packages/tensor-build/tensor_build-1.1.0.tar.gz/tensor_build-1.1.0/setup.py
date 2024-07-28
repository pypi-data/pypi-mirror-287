# setup.py
from setuptools import setup, find_packages

setup(
    name='tensor_build',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'tensorflow>=2.0',
        # other dependencies
    ],
    author='Darren, Eddie, Kahan, Richard',
    description='A block-based framework for TensorFlow',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/stony-su/starterhacks',
)
