from setuptools import setup

setup(
    name='pwned',
    version='0.1',
    url='https://github.com/ctomkow/pwned',
    author='Craig Tomkow',
    author_email='ctomkow@gmail.com',
    license='MIT',
    packages=['pwned'],
    install_requires=['lastpass-python', 'click', 'requests'],
    zip_safe=False
)
