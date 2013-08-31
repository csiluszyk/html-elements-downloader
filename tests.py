#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from html_elements_downloader import _str_to_b, _unpack


class TestHTMLElementsDownloader(unittest.TestCase):

    def test_str_to_b(self):
        two_byte_end = 'jestę'
        sliced_in_the_middle = _str_to_b(two_byte_end, len(two_byte_end))
        properly_sliced = _str_to_b(two_byte_end, len(two_byte_end) - 1)
        self.assertEqual(sliced_in_the_middle, b'jest')
        self.assertEqual(sliced_in_the_middle, properly_sliced)

    def test_unpack(self):
        self.assertEqual('', _unpack('<br />'))
        self.assertEqual('<a>link</a>', _unpack('<p><a>link</a></p>'))
        self.assertEqual('hedgehog', _unpack('hedgehog'))
        self.assertEqual('<piece>raisins</piece>',
                         _unpack('<cake><piece>raisins</piece></cake>'))
        self.assertEqual('<piece>raisins</piece>',
                         _unpack('<cake><piece>raisins</piece></cake>'))
        self.assertEqual('gift',
                         _unpack(' <wrapping_paper>gift</wrapping_paper>  '))

if __name__ == '__main__':
    unittest.main()
