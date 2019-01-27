from setuptools import setup, find_packages

REQUIRES_PYTHON = '>=3.5.0'

setup(
    name='pwned',
    version='0.0.1',
    url='https://github.com/ctomkow/pwned',
    author='Craig Tomkow',
    author_email='ctomkow@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['lastpass-python', 'click', 'requests'],
    entry_points={
          'console_scripts': ['pwned=pwned.pwned:Pwned'],
      },
    zip_safe=False
)
