import feedparser
import argparse

parser = argparse.ArgumentParser(description="Parse wdr traffic rss feed")
parser.add_argument("roads", help="comma-separated list of roads")
parser.add_argument("-v", "--verbose", help="increase verbosity", action="store_true")
args = parser.parse_args()

feedurl = "http://www.wdr.de/radio/home/nachrichten/feeds/verkehrsmeldungen.xml"
f = feedparser.parse(feedurl)

if (args.verbose):
    print "Last update: " + f.updated

for r in args.roads.split(","):
    road = r.upper()
    if (args.verbose):
        print "Searching " + r.upper() + "..."
    for e in f.entries:
        if (e.title == road):
            if (args.verbose):
                print e
            print "(" + road + ") " + e.description
