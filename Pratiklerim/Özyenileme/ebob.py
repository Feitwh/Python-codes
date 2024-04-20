# -*- coding: utf-8 -*-
def ged(a, b):
    if b == 0:
        return a
    else:
        c = a%b
        a = a - c
        return ged(a, b-1)
print(ged(41, 5))
