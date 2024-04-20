#ÇALIŞMA SORULARI
#SORU 1)
print("DİKDÖRTGEN ALAN VE ÇEVRE HESAPLAMA")
genişlik = float(input("Genişlik giriniz:"))
uzunluk = float(input("Uzunluk giriniz:"))

alan = genişlik*uzunluk
çevre = (genişlik+uzunluk)* 2
print("Alan:",alan)
print("Çevre:",çevre)

#SORU 2)
x = int(input("x sayısını girin:"))
y = int(input("y sayısını girin:"))
a = x**y
print("x üzeri y'nin cevabı:",a)
import math
print("x sayısının 2 tabanında logaritması",math.log2(x)) 

#SORU 3)
n = int(input("Bir n sayısı giriniz:"))
if int(n % 2 == 0):
   a = n/2
   print("Sayınız 2'ye bölünüyor ve cevabı:",a)
else: print("Sayınız 2'ye bölünmüyor")
if int(n % 3 == 0):   
    b = n/3
    print("Sayınız 3'e bölünüyor ve cevabı:",b)
else: print("Sayınız 3'e bölünmüyor")    

#SORU 4)
print("x^2 + bx + c = 0 denklemini çözdürünüz.")
b = int(input("b tamsayısını giriniz:"))
c = int(input("c tamsayısını giriniz:"))
diskriminat = b**2 - 4*c
print("2.dereceden denklemin diskriminatı:", diskriminat)
if diskriminat > 0 :
    import math
    kök = ((-b + math.sqrt(diskriminat)))/2
    ikincikök = ((-b - math.sqrt(diskriminat)))/2
    print("Denklemin 1. kökü", kök)
    print("Denklemin 2.kökü", ikincikök)
else: print("Diskriminantınız 0'dan büyük değil.")
if diskriminat == 0 :
    kök = ((-b + math.sqrt(diskriminat)))/2
    print("Denklemin çakışık kökü vardır ve değeri:", kök)
else :print("Diskriminantınız 0'dan küçük olduğu için bu denklemin reel kökü yoktur.")

#SORU 5)
print("ABD seçimlerinin aday kriterleri")
yaş= int(input("Yaşınızı giriniz:"))
vatandaş= int(input("ABD vatandaşı iseniz 1 değilseniz 0 rakamını giriniz:"))
yaşam= int(input("Kaç yıldır ABD'de yaşıyorsunuz giriniz:"))
if yaş > 35 & vatandaş == 1 & yaşam >= 14 : 
    print("3 kriteride karşıladınız tebrikler seçime katılmaya hak kazandınız başarılar!!")
else: print("Maalesef ki bütün kriterleri karşılayamadınız. Unutmayınız ki yaşınızın 35'ten büyük olması, ABD vatandaşı olmanız ve 14 veya 14 yıldan uzun süredir ABD'de yaşıyor olmanız gerekmektedir!!" )