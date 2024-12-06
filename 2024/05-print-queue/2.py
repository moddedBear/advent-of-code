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

def process_deps(update_deps, new_order, page):
    if page not in update_deps or page in new_order: return
    for dep in update_deps[page]:
        process_deps(update_deps, new_order, dep)
        if dep not in new_order:
            new_order.append(dep)

def reorder(pages):
    update_deps = {}
    new_order = []
    # first create a new dep dict so we don't have to think about pages not included in this update
    for page in pages:
        if page in deps:
            # there are global dependencies for this page
            for dep in deps[page]:
                if dep in pages:
                    # this dependency is included in this update, so add it to our update_deps
                    if page not in update_deps:
                        update_deps[page] = []
                    update_deps[page].append(dep)
    
    # add pages that don't have any dependencies
    for page in pages:
        if page not in update_deps:
            # page doesn't have any dependencies so let's print it next
            new_order.append(page)
    
    for page in list(update_deps):
        process_deps(update_deps, new_order, page)
    return new_order

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
            if not is_ordered(pages.copy()):
                print(f'Not in order: {pages}')
                pages = reorder(pages)
                print(f'After reorder: {pages}\n')
                middle = pages[len(pages)//2]
                result += middle
    
    print(result)