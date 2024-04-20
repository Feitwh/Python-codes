# -*- coding:utf-8 -*-
#SAYI TAHMİN OYUNU
import random

print("Sayı tahmin etme oyununa hoş geldiniz!!")
oynamak_istiyor_musun = "Evet"

while oynamak_istiyor_musun == "Evet":
    cevap = random.randint(1, 99)
    tahmin = int(input("1 ile 100 arasındaki sayıyı tahmin et!"))
    sayac = 1

    while tahmin != cevap:
        if tahmin > cevap:
            print("Yanlış tahmin, daha küçük bir sayı dene!!")
        if tahmin < cevap:
            print("Yanlış tahmin, daha büyük bir sayı dene!!")
        tahmin = int(input("Tekrar dene:"))
        sayac +=1
        if sayac > 9:
            print("10 deneme hakkınızı bitirdiniz ve kaybettiniz. Doğru cevap:", cevap)
            break 
        if tahmin == cevap :
            print("Tebrikler, kazandınız!! Doğru tahmin:", cevap)
    oynamak_istiyor_musun = input("Tekrar oynamak ister misin? 'Evet', 'Hayır': ")