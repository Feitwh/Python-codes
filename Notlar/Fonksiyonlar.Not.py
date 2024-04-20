# -*- coding: utf-8 -*-
#FONKSİYONLAR 
#YOUTUBE 1. DERS MAP, FİLTER, LAMBDA
def karesini_al(x):
    return x**2
#Map herhangi bir fonksiyonu listenin elemanlarına uygulatır.
sayılar = [*range(1,6)]
print(sayılar)
print([*map(karesini_al, sayılar)])

#Filter
def çift_sayıları_filtrele(x):
    if x%2 == 0:
        return x
    else:
        return None
print(çift_sayıları_filtrele(3))

sayılar = [*range(1,6)]
print([*filter(çift_sayıları_filtrele, sayılar)])

#Lambda
sayılar = [*range(1,6)]
print([*map(lambda x: x**2, sayılar)])

sayılar = [*range(1,6)]
print([*filter(lambda x: x if x%2==0 else None, sayılar)])
#------------------------------------------------------------------------------
def sayı_girdisi_kontrol_döngü():
        girdi = input("Bir sayı giriniz:")
        
        while not girdi.isdigit():
            print("Üzgünüm! Bu bir sayı değildir.")
            girdi = input("Bir sayı giriniz:")
        
        else:
            print("Tebrikler! Bu bir sayıdır teşekkürler.")
sayı_girdisi_kontrol_döngü()
#------------------------------------------------------------------------------