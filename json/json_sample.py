#!/usr/bin/env python3
'''
    json_sample.py
    Jeff Ondich, 18 April 2025

    A little bit about json: JavaScript Object Notation
'''
import sys
import json

with open('movies.txt') as f:
    movies = json.loads(f.read())

print(movies)
print('================')
print(json.dumps(movies))
print('================')
print(json.dumps(movies, indent=4))

