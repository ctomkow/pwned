# pwned
Check whether a password exists in haveibeenpwned database. Either provide a single password as a cli command, interactively (to hide the password), or pull from a lastpass account.

### Install

1. `pip3 install git+https://github.com/ctomkow/pwned.git`

OR (if you like virtual python environments)

1. `python3 -m virtualenv venv`

2. `source venv/bin/activate`

3. `pip3 install git+https://github.com/ctomkow/pwned.git`

`pwned --help`

### Usage

* `pwned password -i`

* `pwned lastpass -u username@domain.com -i -h`


