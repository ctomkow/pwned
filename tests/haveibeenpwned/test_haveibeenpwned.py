#!/usr/bin/env python3

# system imports
import unittest
import hashlib

# local imports
from .. import context
from haveibeenpwned.haveibeenpwned import HaveIBeenPwned


class test_HaveIBeenPwned(unittest.TestCase):

    def setUp(self):

        self.hash_obj = hashlib.sha1()

        self.pass_1 = 'aaaaazzzzz'
        self.pass_2 = ''
        self.pass_3 = None

        self.prefix = 'aaaaa'
        self.suffix = 'zzzzz'
        self.list_1 = ['aaaaa', 'bbbbb']

    def test_hash_password(self):

        hash1 = HaveIBeenPwned._hash_password(self, self.pass_1)
        self.hash_obj.update(self.pass_1.encode())
        self.assertTrue(self.hash_obj.hexdigest().upper() == hash1)

        self.assertRaises(ValueError, HaveIBeenPwned._hash_password, self, self.pass_2)
        self.assertRaises(ValueError, HaveIBeenPwned._hash_password, self, self.pass_3)

    def test_split_hash(self):

        pre, suf = HaveIBeenPwned._split_hash(self, self.pass_1)
        self.assertEqual(pre, self.prefix)
        self.assertEqual(suf, self.suffix)

    def test_exists(self):

        self.assertTrue(HaveIBeenPwned._exists(self, self.prefix, self.list_1))
        self.assertFalse(HaveIBeenPwned._exists(self, self.suffix, self.list_1))


if __name__ == '__main__':
    unittest.main()
