import unittest

from html_elements_downloader import _str_to_b, _unpack, get_HTML_element, \
    FeedNotExists


class TestHTMLElementsDownloader(unittest.TestCase):

    def test_str_to_b(self):
        two_byte_end = 'jestę'
        sliced_in_the_middle = _str_to_b(two_byte_end, len(two_byte_end))
        properly_sliced = _str_to_b(two_byte_end, len(two_byte_end) - 1)
        self.assertEqual(sliced_in_the_middle, b'jest')
        self.assertEqual(sliced_in_the_middle, properly_sliced)

    def test_get_HTML_element(self):
        feed = '<feed xmlns="http://www.w3.org/2005/Atom"><entry>' \
               '<link type="text/html" href="http://www.example.com/"/>' \
               '</entry></feed>'
        with self.assertRaises(FeedNotExists):
            get_HTML_element(feed, 1, '/')

    def test_unpack(self):
        self.assertEqual('', _unpack('<br />'))
        self.assertEqual('<a>link</a>', _unpack('<p><a>link</a></p>'))
        self.assertEqual('hedgehog', _unpack('hedgehog'))

if __name__ == '__main__':
    unittest.main()
