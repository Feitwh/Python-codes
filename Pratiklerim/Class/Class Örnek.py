# -*- coding: utf-8 -*-
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x                                  
        self.y = y
     
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2                      
        y_diff_sq = (self.y-other.y)**2                      
        return (x_diff_sq + y_diff_sq)**0.5
    
    def inverse(self):
        return Coordinate(self.y, self.x)

c = Coordinate(3, 4)                                                   
origin = Coordinate(0, 0)
print(c.x, origin.x)

print(c.distance(origin))
print(origin.distance(c))

print(Coordinate.distance(c,origin))

print(c)
print(Coordinate(3, 4))

print(c.inverse())

class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom                                        
    
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    
    def __add__(self, other):
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    
    def __sub__(self, other):
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    
    def __float__(self):
        return self.num/self.denom
    
    def inverse(self):
        return Fraction(self.denom, self.num)
    
    def mul(self, other):
        top = self.num*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    
a = Fraction(1, 4)
b = Fraction(3, 4)
c = a + b
d = a.mul(b)

print(c)
print(d)

print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))

def çalışan():
    kabiliyetleri = []
    unvanı = "işçi"
    print(kabiliyetleri)
    print(unvanı)
    
class Çalışan():
    def __init__(self):
        self.kabiliyetleri = []
        print(self.kabiliyetleri)
        
ahmet = Çalışan()
print(ahmet.kabiliyetleri)

class Çalışan():
    kabiliyetleri = ["sınıf niteliği"]
    
    def __init__(self):
        self.kabiliyetleri = ['örnek niteliği']
        
ahmet = Çalışan()
print(ahmet.kabiliyetleri)
print(Çalışan.kabiliyetleri)

class Çalışan():
    personel = []
    
    def __init__ (self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()
        
    def personele_ekle(self):
        self.personel.append(self.isim)
        print("{} adlı kişi personele eklendi.".format(self.isim))
              
    def personeli_görüntüle(self):
        print("Personel listesi: ")
        for kişi in self.personel:
            print(kişi)
            
    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
        
    def kabiliyetleri_görüntüle(self):
        print("{} adlı kişinin kabiliyetleri: ".format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)

c1 = Çalışan("Berke")
c2 = Çalışan("Caner")
print(c1.personel)

c1.isim = "Berk"
c1.personel[0] = "Berk"
print(c1.isim)
print(c1.personel)

c2.kabiliyet_ekle("girişken")
c2.kabiliyet_ekle("konuşkan")
c2.kabiliyetleri_görüntüle()