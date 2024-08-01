from collections import namedtuple

point = (99,23,105)

Point = namedtuple("Point", ["x","y","z"])

p = Point(99,23,105)

print(p, p.x)