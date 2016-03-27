import feedparser
import argparse

feedurl = "http://www.wdr.de/radio/home/nachrichten/feeds/verkehrsmeldungen.xml"

f = feedparser.parse(feedurl)

parser = argparse.ArgumentParser(description="Parse wdr traffic rss feed")
parser.add_argument('roads', help='comma-separated list of roads')

args = parser.parse_args()

for r in args.roads.split(","):
    road = r.upper()
    #print "Road " + r.upper()
    for e in f.entries:
        if (e.title == road):
            print "(" + road + ") " + e.description
