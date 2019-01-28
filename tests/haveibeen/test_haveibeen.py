#!/usr/bin/env python3

# system imports
import unittest
import logging

# local imports
from .. import context
from haveibeen.haveibeen import HaveIBeen


class test_UpgradeCode(unittest.TestCase):

    def setUp(self):

        self.test_prefix = 'aaaaa'
        self.test_suffix = 'zzzzz'
        self.test_list1 = ['xxxxx', 'yyyyy']
        self.test_list2 = ['xxxxx', 'yyyyy', 'zzzzz']
        self.test_list3 = ['zzzzz', 'xxxxx', 'yyyyy', 'zzzzz']

    def test_search_list(self):

        found_list1 = HaveIBeen._search_list(self, self.test_prefix, self.test_suffix, self.test_list1)
        found_list2 = HaveIBeen._search_list(self, self.test_prefix, self.test_suffix, self.test_list2)
        found_list3 = HaveIBeen._search_list(self, self.test_prefix, self.test_suffix, self.test_list3)
        self.assertFalse(found_list1)
        self.assertTrue(found_list2.pop() == 'aaaaazzzzz')
        self.assertTrue(len(found_list3) == 2)


if __name__ == '__main__':
    unittest.main()