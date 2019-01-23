#!/usr/bin/env python3

# core imports
import getpass

# 3rd party imports
import lastpass


class LastPass:

    def __init__(self):

        pass

    def connect(self, username, password, mfa_code):

        password = getpass.getpass("lastpass password:")
        mfa_code = getpass.getpass("lastapss mfa code:")
        vault = lastpass.Vault.open_remote(username, password, mfa_code)

        for i in vault.accounts:
            print(i.id, i.username, i.password, i.url)
