# -*- coding: utf-8 -*-
class BankaHesabı():
    banka_hesapları = 0
    
    def __init__ (self, kimlik_no, başlangıç_bakiyesi):
        self.kimlik_no = kimlik_no
        self.başlangıç_bakiyesi = başlangıç_bakiyesi
        BankaHesabı.güncelle()
        
    @classmethod 
    def güncelle(cls):
        cls.banka_hesapları += 1
        
    @classmethod 
    def banka_method(cls):
        return cls.banka_hesapları 
    
    def para_çek(self):
        print("Bakiye: {} TL".format(self.başlangıç_bakiyesi))
        çekilecek_miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
        
        if self.başlangıç_bakiyesi - çekilecek_miktar < 0:
            print("Yetersiz bakiye lütfen yeterli miktar para çekiniz.")
            
        else:
            self.başlangıç_bakiyesi -= çekilecek_miktar
            print("Para çekme işlemi başarılı. Kalan bakiyeniz: {} TL".format(self.başlangıç_bakiyesi))
            
    def para_yatır(self):
        print("Bakiye: {} TL".format(self.başlangıç_bakiyesi))
        yatırılacak_miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
        
        self.başlangıç_bakiyesi += yatırılacak_miktar
        print("Para yatırma işlemi başarılı. Yeni bakiyeniz: {}".format(self.başlangıç_bakiyesi))
        
            
a = BankaHesabı(22, 1000)
print(a.banka_method())
b = BankaHesabı(10, 2000)
print(b.banka_method())
a.para_çek()
a.para_çek()
a.para_çek()
a.para_yatır()
