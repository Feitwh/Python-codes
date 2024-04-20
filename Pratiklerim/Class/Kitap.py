# -*- coding: utf-8 -*-
class Kitap():
    
    def __init__(self, başlık, yazar, tür, ücret):
        self.başlık = başlık
        self.yazar = yazar
        self.tür = tür
        self.ücret = ücret
        
    def __str__(self):
        return "-" + str(self.başlık) + "," + str(self.yazar) + "," + str(self.tür) + "," + str(self.ücret) + "-"
    
    def detaylar(self):
        return " Kitabın adı: {}\n Yazarın adı: {}\n Türü: {}\n Ücreti: {}".format(self.başlık, 
                                                         self.yazar,
                                                         self.tür,
                                                         self.ücret)
        
kitap1 = Kitap("Denemeler", "Montaıgne", "Roman", "70 TL" )
kitap2 = Kitap("Kürk Mantolu Madonna", "Sabahattin Ali", "Roman", "80 TL")
print(kitap1.detaylar())
print()
print(kitap2.detaylar())