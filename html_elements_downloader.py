import sys

from argparse import ArgumentParser

class FeedNotExists(Exception):
    pass

class HTMLElementNotExists(Exception):
    pass

def get_HTML_element(f, n, s):
    """Returns a byte representation of HTML element.

       :param f: RSS feed URL
       :type f: str
       :param n: number of feed item (numered from one)
       :type n: int
       :param s: xpath to element
       :type s: str
    """
    from feedparser import parse
    from lxml import etree
    from urllib.request import urlopen

    feed = parse(f)

    # EAFP > LBYL
    try:
        response = urlopen(feed['items'][n]['link'])
    except IndexError:
        raise FeedNotExists('Feed {0} doesn\'t  exists!'.format(n))

    tree = etree.parse(response, etree.HTMLParser())

    try:
        s = etree.tostring(tree.xpath(s)[0])
    except IndexError:
        raise HTMLElementNotExists()
    print(s)

def main():
    parser = ArgumentParser(
            description= 'Download HTML element from given RSS feed.')
    parser.add_argument('-f', required=True)
    parser.add_argument('-n', required=True)
    parser.add_argument('-s', required=True)
    args = parser.parse_args()

    try:
        numbers = set(map(int, args.n.split(',')))
    except ValueError:
        sys.exit('Invalid given numbers!')

    for n in numbers:
        try:
            get_HTML_element(f=args.f, n=n, s=args.s)
        except FeedNotExists:
            sys.stderr.write('Feed item no. {0} doesn\'t  exists!'.format(n))
        except HTMLElementNotExists:
            sys.stderr.write('Invalid  xpath!')

if __name__ == "__main__":
    main()
