#!/usr/bin/env python

import recur
import sys

car = [ u'Ferrari',u'F430',u'2016',
            [ u'Body', u'Engine', u'Gear',
                            [u'Wheel', u'Tires', u'Windshield']]]

#recur.recur_print(sys.path,True,1)
#recur.recur_print(car,True,2)
recur.recur_print(car,2)

