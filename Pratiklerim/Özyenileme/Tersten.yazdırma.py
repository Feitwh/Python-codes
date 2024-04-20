# -*- coding: utf-8 -*-
def tersten_yazdırma(metin):
    if len(metin) == 0:
        return metin
    else:
        return tersten_yazdırma(metin[1:]) + metin[0]
print(tersten_yazdırma("terlik"))