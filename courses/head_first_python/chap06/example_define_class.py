#!/usr/bin/env python

class Athlete :
    def __init__(self, a_name, a_dob=None, a_times=[]) :
        self.name = a_name
        self.dob = a_dob
        self.times = a_times


sarah = Athlete('Sarah Sweeney','2002-6-17',['2.18', '2.21', '2.22'])
james = Athlete('James Jones')

print james
print type(james)

print sarah
print type(sarah)

print sarah.name
print sarah.times
print sarah.dob
