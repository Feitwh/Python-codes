# -*- coding: utf-8 -*-
class Menü():
    
    def __init__(self, isim, vejetaryen_mı, fiyat):
        self.isim = isim
        self.vejetaryen_mı = vejetaryen_mı
        self.fiyat = fiyat
        
class Kahvaltı(Menü):
    
    def __init__(self, isim, vejetaryen_mı, fiyat, kahvaltı_fiyatı):
        
        Menü.__init__(self, isim, vejetaryen_mı, fiyat)
        assert 0 < kahvaltı_fiyatı <= 10
        self.kahvaltı_fiyatı = kahvaltı_fiyatı

    def menüye_ekle(self, menü_listesi):
        menü_listesi.append(self)
        print(f"{self.isim} menü listesine eklendi.")

# Menü sınıfından türetilen nesneler
yemek1 = Menü("Döner", False, 24)
yemek2 = Kahvaltı("Mantarlı Omlet", True, 12, 8)

# Menü nesnelerini içeren liste
menü_listesi = [yemek1]

# Kahvaltı sınıfındaki menüye ekleme fonksiyonunu kullanarak yemek2'yi ekleyelim
yemek2.menüye_ekle(menü_listesi)

# Menü denetleme fonksiyonu
def menü_denetle(menü_listesi):
    for menü in menü_listesi:
        if isinstance(menü, Kahvaltı):
            if menü.kahvaltı_fiyatı > 10:
                menü.kahvaltı_fiyatı = 9
            print(f"{menü.isim} yemeğinin fiyatı istenilen aralıktadır.")
        else:
            print(f"{menü.isim} yemeği Kahvaltı sınıfından değil.")
    
menü_denetle(menü_listesi)
