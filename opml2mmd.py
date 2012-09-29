import opml
import sys

outline = opml.parse(sys.argv[1])
print len(outline)