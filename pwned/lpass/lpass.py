#!/usr/bin/env python3

# core imports
from sys import exit

# 3rd party imports
import lastpass


class LPass:

    def __init__(self, username='', password='', mfa=''):

        self.username = username
        self.password = password
        self.mfa      = mfa

        self.id_list       = []
        self.username_list = []
        self.password_list = []
        self.url_list      = []

    def connect(self):

        try:
            return lastpass.Vault.open_remote(self.username, self.password, self.mfa)
        except lastpass.LastPassIncorrectGoogleAuthenticatorCodeError:
            exit('missing or incorrect Google Authenticator code')
        except lastpass.LastPassInvalidPasswordError:
            exit('missing or incorrect lastpass password')
        except lastpass.LastPassUnknownUsernameError:
            exit('missing or incorrect lastpass username')

    def get_vault(self, vault):

        for i in vault.accounts:
            self.id_list.append(i.id.decode("utf-8"))
            self.username_list.append(i.username.decode("utf-8"))
            self.password_list.append(i.password.decode("utf-8"))
            self.url_list.append(i.url.decode("utf-8"))

        return self.id_list, self.username_list, self.password_list, self.url_list
