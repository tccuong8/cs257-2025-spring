#!/usr/bin/env python3
'''
    csv2json.py
    Jeff Ondich, 14 April 2025

    A tiny example of how to use the csv and json modules to convert from
    our simplest books.csv form to an equivalent books.json form.
    The books.csv format is

        title,publication-date,author(s)

    Definitely more to do, but that's a start.
'''
import sys
import csv
import json

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} csvfile')
    exit()

csvfile = sys.argv[1]
with open(csvfile) as f:
    reader = csv.reader(f)
    books = []
    for book_row in reader:
        books.append({'title':book_row[0], 'publication_year':book_row[1], 'authors':book_row[2]})

    print(json.dumps(books, indent=4))
