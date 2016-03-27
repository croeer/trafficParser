import feedparser
import argparse

feedurl = "http://www.wdr.de/radio/home/nachrichten/feeds/verkehrsmeldungen.xml"

f = feedparser.parse(feedurl)
