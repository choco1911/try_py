#!/usr/bin/env python

# Define class
#class Athlete :
#    def __init__(self) :
    


# Creating object instances

#a = Athlete()
#b = Athlete()
#c = Athlete()
#d = Athlete()

#class Athlete:
#    def __init__(self, value=0):
#        self.name = value          # attribut ekzemplyara klassa
#    def how_big(self):              # methon ekzemplyara klassa
#        return(len(self.name))
#
#a = Athlete("Vasya")
#print a.name
#print a.how_big()


class Athlete:
    def __init__(self, value=0):
        self.name = value          # attribut ekzemplyara klassa
    def out(self):                 # methon ekzemplyara klassa
        print self.name

a = Athlete("Vasya")
print a.name
a.out()
