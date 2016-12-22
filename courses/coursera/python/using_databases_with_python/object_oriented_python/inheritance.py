#!/usr/bin/env python


class PartyAnimal() :
    x=0
    name=""

    def __init__(self, nam) :
        self.name = nam
        print self.name,"constructed", "x =", self.x

    def party(self) :
        self.x = self.x + 1
        print self.name,"party count",self.x

class FootballFan(PartyAnimal) :
    points=0

    def touchdown(self) :
        self.points = self.points + 7
        self.party()
        print self.name,"points",self.points 


j = PartyAnimal("Zedan")
j.party()

s = FootballFan("Ronaldo")
s.party()
s.touchdown()


