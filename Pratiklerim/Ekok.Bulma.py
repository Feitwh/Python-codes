# -*- coding: utf-8 -*-
def okek_bul(sayi1, sayi2):
    # İki sayının çarpımını al
    carpim = sayi1 * sayi2
    
    # Büyük sayıyı bul
    buyuk_sayi = max(sayi1, sayi2)
    
    # Büyük sayıya kadar olan sayıları kontrol et
    for i in range(buyuk_sayi, carpim + 1):
        # Her iki sayının da katı olup olmadığını kontrol et
        if i % sayi1 == 0 and i % sayi2 == 0:
            return i  # İlk bulunan ortak katı döndür
    
    return carpim  # Eğer hiç ortak kat bulunamazsa, çarpımı döndür

# Kullanıcıdan input al
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

# OKEK'i bul ve ekrana yazdır
okek = okek_bul(sayi1, sayi2)
print(f"{sayi1} ve {sayi2} sayılarının OKEK'i: {okek}")