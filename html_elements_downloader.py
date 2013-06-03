#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser


class FeedNotExists(Exception):
    pass


class HTMLElementNotExists(Exception):
    pass


def get_HTML_element(f, n, s):
    """Returns a string representation of HTML element.

       :param f: RSS feed URL
       :type f: str
       :param n: number of feed item (numbered from one)
       :type n: int
       :param s: xpath to element
       :type s: str
    """
    from feedparser import parse
    from lxml import etree
    from lxml.html.clean import clean_html
    from urllib.request import urlopen

    feed = parse(f)

    try:
        response = urlopen(feed['items'][n]['link'])
    except IndexError:
        raise FeedNotExists('Feed {0} doesn\'t  exists!'.format(n))

    enc = response.headers.get('content-type', 'utf-8').split('charset=')[-1]
    tree = etree.parse(response, etree.HTMLParser())

    try:
        el = clean_html(etree.tostring(tree.xpath(s)[0]))
    except IndexError:
        raise HTMLElementNotExists()

    try:
        el = el.decode(enc, 'ignore')
    except LookupError:
        el = el.decode('utf-8', 'ignore')

    return el


def _str_to_b(s, n=255, enc='utf-8'):
    # Use this function to convert sting [s] in order to save it in database
    # which accepts characters in [enc] encoding of max length [n]

    # After slicing we can produce invalid character in given encoding
    # so we must decode [s] and encode it again.
    return s.encode(enc)[:n].decode(enc, 'ignore').encode(enc)


def main():
    parser = ArgumentParser(
        description= 'Download HTML element from given RSS feed.')
    parser.add_argument('-f', required=True)
    parser.add_argument('-n', required=True)
    parser.add_argument('-s', required=True)
    args = parser.parse_args()

    # EAFP > LBYL
    try:
        numbers = set(map(int, args.n.split(',')))
    except ValueError:
        sys.exit('Invalid given numbers!')

    for n in numbers:
        try:
            print(get_HTML_element(f=args.f, n=n, s=args.s))
        except FeedNotExists:
            sys.stderr.write('Feed item no. {0} doesn\'t  exists!'.format(n))
        except HTMLElementNotExists:
            sys.stderr.write('Invalid  xpath!')

if __name__ == "__main__":
    main()
