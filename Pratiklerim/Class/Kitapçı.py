# -*- coding: utf-8 -*-
class Kitap:
    def __init__(self, baslik, yazar):
        self.baslik = baslik
        self.yazar = yazar

class Kitapci:
    def __init__(self, adi):
        self.adi = adi
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"{kitap.baslik} kitabı {self.adi} kitapçısına eklendi.")

    def kitap_cikar(self, kitap):
        if kitap in self.kitaplar:
            self.kitaplar.remove(kitap)
            print(f"{kitap.baslik} kitabı {self.adi} kitapçısından çıkarıldı.")
        else:
            print(f"{kitap.baslik} kitabı {self.adi} kitapçısında bulunamadı.")

    def kitap_ara(self, anahtar):
        bulunan_kitaplar = [kitap for kitap in self.kitaplar if anahtar.lower() in kitap.baslik.lower() or anahtar.lower() in kitap.yazar.lower()]

        if bulunan_kitaplar:
            print(f"Arama Sonuçları ({self.adi} Kitapçısı):")
            for kitap in bulunan_kitaplar:
                print(f"- {kitap.baslik} (Yazar: {kitap.yazar})")
        else:
            print(f"Aranan '{anahtar}' kelimesi ile eşleşen kitap bulunamadı.")

# Örnekler
kitap1 = Kitap("Harry Potter ve Felsefe Taşı", "J.K. Rowling")
kitap2 = Kitap("Dune", "Frank Herbert")
kitap3 = Kitap("1984", "George Orwell")

kitapci1 = Kitapci("Kitapçı 1")
kitapci2 = Kitapci("Kitapçı 2")

kitapci1.kitap_ekle(kitap1)
kitapci1.kitap_ekle(kitap2)
kitapci2.kitap_ekle(kitap3)

kitapci1.kitap_ara("Harry Potter")
kitapci2.kitap_ara("George Orwell")

kitapci1.kitap_cikar(kitap2)
kitapci2.kitap_ara("Dune")
