#!/usr/bin/python
# -*- coding: utf-8 -*-

import fnmatch
import getopt
import os
import sys

def main(argv):
    search_path = "."
    pattern = "*.*"

    try:
        opts, args = getopt.getopt(argv, "d:p:", ["directory=", "pattern="])
    except getopt.GetoptError:
        print("error")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-d", "--directory"):
            search_path = arg
        elif opt in ("-p", "--pattern"):
            pattern = arg

    for root, dirnames, filenames in os.walk(search_path):
        for filename in fnmatch.filter(filenames, pattern):
            path = os.path.join(root, filename)
            print('\\lstinputlisting[title=\large{%s}]{%s}' % (filename,  path.replace('\\', '/')))




if __name__ == "__main__":
    main(sys.argv[1:])
