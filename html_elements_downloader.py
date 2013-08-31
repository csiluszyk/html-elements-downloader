#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from multiprocessing import Process, Lock

from feedparser import parse
from lxml import etree
from lxml.html.clean import clean_html
from urllib.request import urlopen
from argparse import ArgumentParser


class FeedNotExists(Exception):
    pass


class HTMLElementNotExists(Exception):
    pass


def _unpack(s):
    s = s.strip()
    # Returns a given string without first and last HTML tag.
    if s and s[0] == '<' and s[-1] == '>':
        return s[s.find('>') + 1:s.rfind('<')]
    else:
        return s


def get_HTML_element(xpath, url):
    """Returns a string representation of HTML element
       given in `xpath` from `url`.

       :param xpath: xpath to element
       :type xpath: str
       :param url: URL address from which `xpath` will be downloaded
       :type url: str
    """

    response = urlopen(url)
    enc = response.headers.get('content-type', 'utf-8').split('charset=')[-1]
    tree = etree.parse(response, etree.HTMLParser())

    try:
        el = clean_html(etree.tostring(tree.xpath(xpath)[0]))
    except IndexError as e:
        raise HTMLElementNotExists(
            'HTML element for item %s doesn\'t exist!' % n) from e

    try:
        el = el.decode(enc, 'ignore')
    except LookupError:
        el = el.decode('utf-8', 'ignore')

    return _unpack(el)


def _str_to_b(s, n=255, enc='utf-8'):
    # Use this function to convert sting `s` in order to save it in database
    # which accepts characters in `enc` encoding of max length of `n` bytes.

    # After slicing we can produce invalid character in given encoding
    # so we must decode `s` and encode it again.
    return s.encode(enc)[:n].decode(enc, 'ignore').encode(enc)


def main(xpath, url):
    try:
        result = get_HTML_element(xpath, url)
    except HTMLElementNotExists as e:
        result = str(e)

    lock.acquire()
    print(result)
    lock.release()


def get_args():
    parser = ArgumentParser(
        description='Download HTML element from given RSS feed.')
    parser.add_argument('-f', required=True)
    parser.add_argument('-n', required=True)
    parser.add_argument('-x', required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    # EAFP > LBYL
    try:
        # we want to unique numbers, numbered from 0
        numbers = set(map(lambda x: int(x), args.n.split(',')))
    except ValueError:
        sys.exit('Invalid given numbers!')

    lock = Lock()

    feed = parse(args.f)

    for n in numbers:
        try:
            url = feed['items'][n]['link']
        except IndexError as e:
            raise FeedNotExists('Item %s doesn\'t  exist!' % n) from e
        else:
            Process(target=main, args=(args.x, url)).start()
