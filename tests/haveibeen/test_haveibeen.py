#!/usr/bin/env python3

# system imports
import unittest
import hashlib

# local imports
from .. import context
from haveibeen.haveibeen import HaveIBeen


class test_UpgradeCode(unittest.TestCase):

    def setUp(self):

        self.hash_obj = hashlib.sha1()
        self.test_pass1 = 'password1'
        self.test_pass2 = ''
        self.test_pass3 = None

        self.test_suffix = 'zzzzz'
        self.test_list1 = ['xxxxx', 'yyyyy']
        self.test_list2 = ['xxxxx', 'yyyyy', 'zzzzz']

    def test_hash_password(self):

        hash1 = HaveIBeen._hash_password(self, self.test_pass1)
        self.hash_obj.update(self.test_pass1.encode())
        self.assertTrue(self.hash_obj.hexdigest().upper() == hash1)

        self.assertRaises(ValueError, HaveIBeen._hash_password, self, self.test_pass2)
        self.assertRaises(ValueError, HaveIBeen._hash_password, self, self.test_pass3)

    def test_exists(self):

        self.assertFalse(HaveIBeen._exists(self, self.test_suffix, self.test_list1))
        self.assertTrue(HaveIBeen._exists(self, self.test_suffix, self.test_list2))


if __name__ == '__main__':
    unittest.main()
