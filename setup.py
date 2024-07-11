from setuptools import setup, find_packages

setup(
    name = 'monte carlo',
    version = '1.0.3',
    author = 'Ashley Miller',
    author_email = 'asm2fe@virginia.edu',
    packages = ['montecarlo'],
    url = 'https://github.com/ashley-m/DS5100-finalproject-asm2fe/tree/main',
    license = 'LICENSE.txt',
    description = 'A monte carlo simulator working on both numerical and alphabetical data',
    long_description = open('README.md').read()
)