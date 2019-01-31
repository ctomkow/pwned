#!/usr/bin/env python3

# core imports
import hashlib
import sys

# 3rd party imports
import requests


class HaveIBeenPwned:

    def __init__(self):

        self.haveibeenpwned_url = "https://api.pwnedpasswords.com/range/"

    def check_password(self, password=''):

        try:
            hashed_pass = self._hash_password(password)
        except ValueError as error:
            raise error

        prefix, suffix = self._split_hash(hashed_pass)
        pwned_hash_suffix_list = self._get_pwned_hashes(prefix)

        if self._exists(suffix, pwned_hash_suffix_list):
            return True
        else:
            return False

    def _hash_password(self, password):

        if not password:
            raise ValueError("Password can not be empty.")

        hash_obj = hashlib.sha1()
        hash_obj.update(password.encode())
        return hash_obj.hexdigest().upper()

    def _split_hash(self, hash):

        prefix = hash[:5]
        suffix = hash[5:]
        return prefix, suffix

    def _exists(self, suffix, hash_list):

        for hash in hash_list:
            if suffix in hash:
                return True
        return False

    def _get_pwned_hashes(self, hash_prefix):

        try:
            req = requests.get(self.haveibeenpwned_url + hash_prefix)
        except requests.exceptions.HTTPError as error:
            # HTTP failure code
            print(error + req.status_code)
            sys.exit(1)
        except requests.exceptions.RequestException as error:
            # catch-all failure
            print(error)
            sys.exit(1)

        return req.text.splitlines()
