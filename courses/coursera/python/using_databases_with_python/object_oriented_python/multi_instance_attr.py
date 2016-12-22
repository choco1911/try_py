#!/usr/bin/env python

class PartyAnimal:
    x=0
    name=""

    def __init__(self, nam):
        self.name = nam
        print self.name,"constructed","x =",self.x
    
    def party(self):
        self.x = self.x + 1
        print self.name,"party count","x =",self.x


s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")

j.party()
s.party()
