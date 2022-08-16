from setuptools import setup, find_packages

REQUIRES_PYTHON = '>=3.5.0'

setup(
    name='pwned',
    version='0.0.6',
    url='https://github.com/ctomkow/pwned.py',
    author='Craig Tomkow',
    author_email='ctomkow@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'click>=7.0',
        'requests>=2.21.0,<=3.0.0',
        'lastpass-python>=0.3.1',
        'click-log>=0.3.2'
    ],
    entry_points={
          'console_scripts': ['pwned=pwned.pwned:Pwned'],
    },
    zip_safe=False
)
