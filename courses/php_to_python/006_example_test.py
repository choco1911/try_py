#!/usr/bin/env python



def rFunc(x):
    if x == 0 : return 1
    return x + rFunc(x - 1)

# 5 + rFunc
# 5 + 4  + rFunc
# 5 + 4 + 3 + rFunc
# 5 + 4 + 3 + 2 + rFunc
# 5 + 4 + 3 + 2 + 1 + rFunc
# 5 + 4 + 3 + 2 + 1 + 1
