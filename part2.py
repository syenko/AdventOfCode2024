import re
import collections
import itertools

class Coord(collections.namedtuple('Coord', ['x', 'y'])):
    def __add__(self, other):
        return Coord(**{field: getattr(self, field) + getattr(other, field)
                        for field in self._fields})
    def __sub__(self, other):
        return Coord(**{field: getattr(self, field) - getattr(other, field)
                        for field in self._fields})

file = open('input.txt')
file = open('test.txt')

lines = [x.strip() for x in file]
