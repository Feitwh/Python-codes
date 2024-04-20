# -*- coding: utf-8 -*-
class Uçuş():
    havayolu = 'THY'
    
    def __init__(self, kod, kalkış, varış, süre, kapasite, yolcu):
        self.kod = kod
        self.kalkış = kalkış 
        self.varış = varış
        self.süre = süre
        self.kapasite = kapasite
        self.yolcu = yolcu
    
    def ananons_yap(self):
        return "{} kodlu uçağımız {} yerinden {} yerine gidecektir. Yolculuk süresi {} dakika olacaktır. İyi yolculuklar dileriz.".format(
            self.kod,
            self.kalkış, 
            self.varış, 
            self.süre)
    
uçuş1 = Uçuş('TK201', 'ORD', 'İST', 60, 50, 40)

print(uçuş1.kapasite)
print()
print(uçuş1)
print()
print(uçuş1.ananons_yap())


