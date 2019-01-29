#!/usr/bin/env python3

# core imports
import hashlib

# 3rd party imports
import requests


class HaveIBeen:

    def __init__(self):

        pass

    def check_password(self, password=''):

        hash_pass = self._hash_password(password)
        hash_prefix = hash_pass[:5]
        hash_suffix = hash_pass[5:]
        url = "https://api.pwnedpasswords.com/range/" + hash_prefix
        req = requests.get(url)

        returned_hash_suffix_list = req.text.splitlines()
        found_hashes = self._search_list(hash_prefix, hash_suffix, returned_hash_suffix_list)

        if not found_hashes:
            return False
        else:
            return True

    def _hash_password(self, password):

        if not password:
            raise ValueError("Incorrect password input. Must be not empty")

        hash_obj = hashlib.sha1()
        hash_obj.update(password.encode())
        return hash_obj.hexdigest().upper()

    def _search_list(self, prefix, suffix, hash_list):

        found_list = []
        for onehash in hash_list:
            if suffix in onehash:
                found_list.append(prefix + onehash)
        return found_list
