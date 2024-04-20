# -*- coding: utf-8 -*-
def kayıt_birleştir(d1,d2):
    for key, value in d2.items():
        if key in d1:
            d1[key] = [sum(x) for x in zip(d1[key], value)]
        else:
            d1[key] = value

    print(d1)
    
kayıt_birleştir({"GS": [8,1], "FB": [6,3]}, {"GS": [2,0], "BJK": [5,4]})