# -*- coding: utf-8 -*-
#YOUTUBE: TRY - EXCEPT - FİNALLY

# round komutu yuvarlama işlemi yapar.

print(round(1.6))
print(round(1.3))

# Normal sayı yuvarlama algoritması:
    
def tam_sayıya_çevir():
    girdi = float(input("Bir ondalık sayı giriniz: "))
    
    print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))

# Try ve except komutlu deney:
# Try ve except if ve else gibi çalışır ama bu komutlar hataları düzeltmek için kullanılır.
# Finally ise Try veya Except çalışsın çalışmasın her türlü çalışan bir komuttur.

def try_tam_sayıya_çevir():
    girdi =input("Bir ondalık sayı giriniz: ")
    
    #print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))
    
    status = " "
    
    try:
        girdi = float(girdi)   
        print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))
        status = "başarılı"
    except:
        print("{} girdisi ondalık tipe çevirlemiyor!".format(girdi))
        status = "başarısız"
    finally:
        print("Tam sayıya çevirme işlemi {} olarak tamamlandı!".format(status))

try_tam_sayıya_çevir()

# Sonsuz döngü kullanarak doğru girdi alınana kadar tekrar ettiren algoritma:

def try_tam_sayıya_çevir_döngü():
    while True:
        girdi =input("Bir ondalık sayı giriniz: ")
        
        try:
            girdi = float(girdi)   
            print("Yuvarlama işleminin sonucu: {}".format(round(girdi)))
            break
        except:
            print("{} girdisi ondalık tipe çevirlemiyor!".format(girdi))
            pass
        
try_tam_sayıya_çevir_döngü()

# Eğer expectten sonra hatayı yazarsanız ona bir çıktı vs yaptırabiliriz:

print()
print("Hatanın adını girerek hatadan kurtulma: ")
try:
    5 + "a"
except TypeError:
    print("Verilen değerler toplanamıyor.")
    
