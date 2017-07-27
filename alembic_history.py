#!/usr/bin/python3

"""Show link of alembic migrations from first to last
"""

import os
from pprint import pprint

PATH = './versions'

class Migration:
    def __init__(self, id, father=None, child=None):
        self.id = id
        self.father = father
        self.child = child

    def __repr__(self):
        return '{} -> {} -> {}'.format(getattr(self.father, 'id', 'None'), self.id, getattr(self.child, 'id', 'None'))


seen = set()
ordered = []
migrations = os.listdir(path=PATH)
for m in migrations:
    try:
        with open(os.path.join(PATH, m), 'r') as f:
            for l in f:
                migration_before = None
                l = l.strip()
                if l.startswith('Revision ID: '):
                    migration_id = l[13:]
                if l.startswith('Revises: '):
                    migration_before = l[9:]
                    break
        print(migration_before, migration_id)
        if migration_before == 'None':
            new = Migration(migration_id)
            ordered.append(new)
        else:
            new = Migration(migration_id, migration_before)
            seen.add(new)
    except IsADirectoryError:
        print('skipping {}'.format(m))

print(ordered, seen)

while seen:
    father = ordered[-1]
    for m in seen:
        if m.father == father.id:
            ordered.append(m)
            seen.discard(m)
            father.child = m
            m.father = father
            break

pprint(ordered)
