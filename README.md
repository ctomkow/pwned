# pwned
[![Build Status](https://travis-ci.org/ctomkow/pwned.svg?branch=master)](https://travis-ci.org/ctomkow/pwned)
[![codecov](https://codecov.io/gh/ctomkow/pwned/branch/master/graph/badge.svg)](https://codecov.io/gh/ctomkow/pwned/)

Check whether a password exists in haveibeenpwned database. Either provide a single password as a cli command, interactively (to hide the password), or pull from a lastpass account.

#### Easy Install

1. `pip3 install git+https://github.com/ctomkow/pwned.git`

#### Manual Install

1. `git clone git+https://github.com/ctomkow/pwned.git`

2. `cd pwned && python3 setup.py install`

#### Virtual Install

1. `python3 -m virtualenv venv`

2. `source venv/bin/activate`

3. `pip3 install git+https://github.com/ctomkow/pwned.git`

#### _If all else fails_ Install
1. `sudo pip3 install git+https://github.com/ctomkow/pwned.git`


### Usage

* `pwned --help`

* `pwned password -i`

* `pwned lastpass -u username@domain.com -i -h`


### Development Notes

For development, use virtualenv for testing (even with an IDE such as PyCharm).
Simply, have a terminal in the venv instance, and `python3 setup.py install`, to test the cli.



