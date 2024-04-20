#YOUTUBE 1. DERS: YAZDIRMA
# \n = new line demek yeni satır geçer.
print("GÜN IŞIĞI \nBir gün...")

# \t = tab kadar araya boşluk bırakır.
print("Uzun bir \t boşluk")

# .format() kullanımlarından biri;
print("Benim adım {}".format('Fatih'))
# ya da sırayı gözeterek ekleyebilir;
print("Benim adım {}, yaşım {}".format('Fatih', 20))

# İndex 0'dan saymaya başlar unutma !!
# Eğer üstteki süslü parantezin içine ilk yaşın yazılması istenirse isteğe bağlı olarak ilk süslü parantez içine 1 yazarsak index sayımı devreye girer ve ona göre dizer:
print("Benim adım {1}, yaşım {0}".format('Fatih', 20))

# Tabi daha iyisi hata olasılığını azaltmak için değişken atamak daha iyi olur:
print("Benim adım {ad}, yaşım {yaş}".format(ad='Fatih',yaş=20))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#YOUTUBE 2. DERS: DEĞİŞKEN VE ATAMA
a ="Çok kolay olduğu için halletik :D"
print(a)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#YOUTUBE 3. DERS: BOOLEAN (BOOL)
#True ya da False
a = True
print (a)
print(type(a))
b = 'True'
print(b)
print(type(b))

yaş2 = 18
print(yaş2 > 20)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#YOUTUBE 4. DERS: LİSTE
liste = ['a','b','c','d','e']
print(liste)

#Listeye eleman eklemek isterseniz sonradan;
liste = liste + ['F']
print(liste)

#append listeye direkt ekleyebilir.
liste.append('g')
print(liste)

#pop sondakini okutur ve listeden çıkarır;
#çıkardığımız elemanı atayalım ve görelim
çıkan_eleman = liste.pop()
print(liste)
print(çıkan_eleman)
# ya da...
liste.pop(2)
print(liste)

#sort komutu sıralama yapar 
#reverse ters sıralama yapar
sayılar = [2312,43,12312,4323,2,1,2,3]
sayılar.sort()
print(sayılar)
sayılar.reverse()
print(sayılar)
alfabe = ['a','s','n','b']
alfabe.sort()
print(alfabe)

#set süslü parantez ile listeler ve tekrar edenleri tekrar göstermez.
set(sayılar)
print(set(sayılar))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#YOUTUBE 5. DERS TUPLE (tup)
#Listelerin aksine değiştirilemezdir (immutable) ve normal parantez ile gösterilir.
liste = ['a','b','c','d','e']
print(liste)
tup = ('a','b','c','d','e','a')
print(tup)

#count listede istediğiniz şeyden kaç tane var onun sayısını verir.
tup.count(a)
print(tup.count(a))

#index, listedeki o elemanın konumunu index olarak gösterir.
#Eğer ki istediğiniz yerden itibaren kaçıncı sıra da diye sordurmak istersek;
tup.index('a',3)
print(tup.index('a',3))
#Eğer listede olmayan bir şeyin yerini sordurursak HATA ALIRIZ.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#YOUTUBE 6. DERS DİCTİONARY (dict)
dict1 = {'isim': 'Fatih', 
         'yaş': '20',
         'şehir': 'Giresun',
         }
print(dict1)

print(dict1['yaş'])
print(dict1['isim'])
#Eğer ki = dict.get yazarsan istediğin bilgi için normal parantez kullanabilirsin.
print(dict1.get('şehir'))
#Keys komutu dictionary'de hangi anahtarlar varsa onları gösterir.
print(dict1.keys())
#Values komutu ise anahtarların karşılığını gösterir.
print(dict1.values())
#İtems komutu satırları tek tek yazar.
print(dict1.items())