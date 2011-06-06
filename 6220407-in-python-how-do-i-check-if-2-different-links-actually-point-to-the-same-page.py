#!/usr/bin/env python
# coding: utf-8

import urllib2

url1 = 'http://www.independent.co.uk/life-style/gadgets-and-tech/news/chinese-blamed-for-gmail-hacking-2292113.html'
url2 = 'http://www.independent.co.uk/life-style/gadgets-and-tech/news/2292113.html'

for url in [url1, url2]:
    result = urllib2.urlopen(urllib2.HeadRequest(url))
    print result.geturl()
