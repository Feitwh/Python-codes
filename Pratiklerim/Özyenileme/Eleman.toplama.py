# -*- coding: utf-8 -*-
def eleman_topla(list):
    if not list :
        return 0
    else:
        a = list.pop(0)
        return a + eleman_topla(list)
        
print(eleman_topla([2, 5, 8, 17]))