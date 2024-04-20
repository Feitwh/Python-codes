# -*- coding: utf-8 -*-
def duzleyen_fonksiyon(lst):
    duzlenmis_liste = []
    
    for eleman in lst:
        if isinstance(eleman, list):
            # Eğer eleman bir liste ise, fonksiyonu tekrar çağırarak iç içe listeyi düzle
            duzlenmis_liste.extend(duzleyen_fonksiyon(eleman))
        else:
            # Eğer eleman bir liste değilse, doğrudan listeye ekle
            duzlenmis_liste.append(eleman)
    
    return duzlenmis_liste

# Test
ornek_liste = [[1, 2], [3, 4]]
sonuc = duzleyen_fonksiyon(ornek_liste)
print(sonuc)


liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

liste1.extend(liste2)

print(liste1)


liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

liste1.append(liste2)

print(liste1)
