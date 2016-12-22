#!/usr/bin/env python


class PartyAnimal() :
    x=0
    name=""

    def __init__(self, nick) :
        self.name = nick
        print "Constructed", self.name, "x =", self.x

    def party(self) :
        self.x = self.x + 1
        print "So far", self.x

class Football(PartyAnimal) :
    steps=0

   # def __init__(self) :

    def foot(self) :
        self.steps = self.steps + 7
        print "Steps", self.steps 


j = PartyAnimal("James")
j.party()

s = Football("RonalDO")
s.party()

s.foot()


