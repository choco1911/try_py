#!/usr/bin/env python

class Athlete :
    f=list()
    def __init__(self, a_name, a_dob=None, a_times=[]) :
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def t(self) :
        # [ print item for item in self.times ]
        for aaa in self.times :
             self.f.append(aaa+'s')

        return self.f
        
            
            
            


sarah = Athlete('Sarah Sweeney','2002-6-17',['3.11', '2.18', '2.21', '2.22'])
#james = Athlete('James Jones')

#print james
#print type(james)
#
#print sarah
#print type(sarah)
#
#print sarah.name
#print sarah.times
#print sarah.dob

print sarah.t()
