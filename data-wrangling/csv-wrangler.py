#!/usr/bin/env python3
'''
    csv-wrangler.py
    Jeff Ondich, 14 April 2025

    A tiny example of how to use the csv module to manipulate
    comma-separated value data. We're focusing here on a books.csv
    file formatted like so:

        title,publication-date,author(s)
'''
import sys
import csv

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} csvfile')
    exit()

csvfile = sys.argv[1]
with open(csvfile) as f:
    reader = csv.reader(f)
    books = []
    for book_row in reader:
        title = book_row[0]
        print(title)
