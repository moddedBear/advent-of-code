#!/usr/bin/env python
import sys

deps = {}

def is_ordered(pages):
    while len(pages):
        if pages[0] in deps:
            for dep in deps[pages[0]]:
                if dep in pages:
                    return False
        pages.pop(0)
    return True

filename = sys.argv[1]
with open(filename, 'r') as f:
    parsing_deps = True
    result = 0
    for line in f:
        if line.strip() == '':
            parsing_deps = False
            continue

        if parsing_deps:
            dep, page = [int(p) for p in line.split('|')]
            if page not in deps:
                deps[page] = []
            deps[page].append(dep)

        else:
            pages = [int(page) for page in line.split(',')]
            middle = pages[len(pages)//2]
            if is_ordered(pages):
                result += middle
    
    print(result)