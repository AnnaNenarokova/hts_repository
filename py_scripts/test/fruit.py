#!/usr/bin/python

class Fruit(object):
    edible = True

def make_sweet(fruit_class):
    setattr(fruit_class, 'taste', 'sweet')

kaki = Fruit()
make_sweet(kaki)

print kaki.taste
print kaki.edible