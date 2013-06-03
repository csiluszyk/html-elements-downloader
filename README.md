html-elements-downloader
========================

html-elements-downloader is a tool for downloading HTML element given in XPath
from specific RSS feed. It supports all major RSS standards
(including RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0)


Installation
------------

Ensure that required system dependencies are installed:

* python3.1
* [virtualenv] (Debian Squeeze package: *python-virtualenv*)
* git

It should be easier to begin with a separate folder at first:

    mkdir htmlelementsdownloader
    cd htmlelementsdownloader

and to install script inside a virtualenv
(assuming that you have *python3.1* in your system path):

    virtualenv --python=python3.1 venv
    . venv/bin/activate

Then script and its dependencies can be installed by simply running:

    git clone git://github.com/czaarek/html-elements-downloader.git
    pip install -e .

After this you can run script, e.g.:

     python html_elements_downloader.py -f http://feeds.feedburner.com/TechCrunch -n 2,4 -s /html/body/div

[virtualenv]: http://www.virtualenv.org/en/latest/index.html

Dependencies
------------

This script uses following third part libraries:

* [argparse] (to parse command line arguments)
* [feedparser] (to parse given RSS feed and get from it sites addresses)
* [lxml] (to get HTML element from XPath)

[argparse]: http://code.google.com/p/argparse/
[feedparser]: http://code.google.com/p/feedparser/
[lxml]: http://lxml.de/
