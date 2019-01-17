#!/usr/bin/env python3

# imports
import requests
import hashlib
import getpass


class CheckPassword:

    def __init__(self):

        self.main()

    def main(self):

        password = getpass.getpass("Input password to check:")
        hash_pass = self.hash_password(password)
        hash_prefix = hash_pass[:5]
        hash_suffix = hash_pass[5:]
        url = "https://api.pwnedpasswords.com/range/" + hash_prefix
        req = requests.get(url)

        returned_hash_suffix_list = req.text.splitlines()

        found_hashes = self.search_list(hash_prefix, hash_suffix, returned_hash_suffix_list)

        if not found_hashes:
            print("CONGRATS, PASSWORD NOT FOUND")

        for ahash in found_hashes:
            print("NUMBER OF MATCHES:", ahash.split(':')[-1])

    def hash_password(self, password):

        hash_obj = hashlib.sha1()
        hash_obj.update(password.encode())
        return hash_obj.hexdigest().upper()

    def search_list(self, prefix, suffix, hash_list):

        found_list = []
        for onehash in hash_list:
            if suffix in onehash:
                found_list.append(prefix + onehash)

        return found_list


if __name__ == '__main__':
    CheckPassword()
