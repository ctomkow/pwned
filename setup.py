from setuptools import setup, find_packages

setup(
    name='pwned',
    version='0.01',
    url='https://github.com/ctomkow/pwned',
    author='Craig Tomkow',
    author_email='ctomkow@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['lastpass-python', 'click', 'requests'],
    entry_points={
          'console_scripts': [
              'pwned = pwned.pwned:Pwned'
          ]
      },
    zip_safe=False
)
