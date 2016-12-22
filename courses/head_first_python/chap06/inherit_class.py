#!/usr/bin/env python


# nasledovanie ot vstroennogo objecta list atributov i methodv 

class NamedList(list) :
    def __init__(self, a_name=None):
        list.__init__([])
        self.name = a_name

johnny = NamedList()
print type(johnny)
print dir(johnny)

print johnny

johnny.name='John Paul Jones'

johnny.append("Bass Player")
johnny.extend(['Composer', "Arranger", "Musician"])

print johnny.name
print johnny

for who in johnny :
    print(johnny.name + ' is a ' + who + '.')
