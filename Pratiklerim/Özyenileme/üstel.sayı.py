# -*- coding: utf-8 -*-
def power(üst, taban):
    if üst == 0:
        return 1
    else:
        return taban* power(üst - 1, taban)
print(power(3,5))