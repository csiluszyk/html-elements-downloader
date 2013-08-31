html-elements-downloader
========================

html-elements-downloader is a tool for downloading HTML content of element
given in XPath from links in RSS feed entries (which are given as
comma-separated numbers). It supports all major RSS standards
(including RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0)


Installation
------------

Ensure that required system dependencies are installed:

* python3
* [virtualenv](http://www.virtualenv.org/en/latest/index.html)
* git

It should be easier to begin with a separate folder at first:

    mkdir htmlelementsdownloader
    cd htmlelementsdownloader

and to install script inside a virtualenv
(assuming that you have *python3* in your system path):

    virtualenv --python=python3 venv
    . venv/bin/activate

Then script and its dependencies can be installed by simply running:

    git clone git://github.com/czaarek/html-elements-downloader.git
    cd html-elements-downloader
    pip install -e .

After this you can run script, e.g.:

    python html_elements_downloader.py -f http://feeds.feedburner.com/TechCrunch -n 0,2,4,6 -x '/html/body/div/div/div/div[3]/div[3]/p'

or run the tests:

    python test.py

Dependencies
------------

This script uses following third part libraries:

* [argparse](http://code.google.com/p/argparse/) (to parse command line arguments)
* [feedparser](http://code.google.com/p/feedparser/) (to parse given RSS feed and get from it sites addresses)
* [lxml](http://lxml.de/) (to get HTML element from XPath)
