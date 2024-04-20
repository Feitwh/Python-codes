#YOUTUBE 1. DERS FOR DÖNGÜSÜ
#İndexleri tek tek görerek işlem yapar.
isimler = ['Fatih', 'Azra']
for kullanıcı in isimler :
    print(kullanıcı)
    
sayaç = 0
for kullanıcı in isimler :
    sayaç += 1
    print(sayaç, kullanıcı)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#YOUTUBE 2. DERS WHİLE DÖNGÜSÜ
#Sonsuz döngüler yapılabilir ama tabi genellikle bu tarz döngüler istemeyiz :)
x = 0 
while x < 10:
    print("{} değeri 10'dan küçüktür".format(x))
    x += 1
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#YOUTUBE 3. DERS RANGE-ENUMERATE-ZİP
#Range;
print(range(10))

print(list(range(10)))
#daha iyi python dilinde yazmak istersen:
print([*range(10)])

#For ile beraber kullanılabilir:
for sayı in range(10):
    print(sayı)
    
#Enumerate;
harfler = ['a', 'b', 'c', 'd', 'e']
for harf in enumerate(harfler):
    print(harf)
    
for index, harf in enumerate(harfler):
    print(index, harf)
    
#Zip;
ülkeler = ['TR', 'FR', 'DE']
sıralamalar = range(1,4)

for ülke in zip(ülkeler,sıralamalar):
    print(ülke)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#YOUTUBE 4. DERS BREAK-CONTİNUE-PASS
#Break;
harfler = ['a', 'b', 'c', 'd', 'e']*100
for index,harf in enumerate(harfler):
    if harf == 'c':
        print('{} harfi {}. indexte!'.format(harf,index))
        break
#100 listeyi tek tek yazmak yerine ilk c yi buldu ve artık aramayı bıraktı.

#Continue;
for sayı in range(1,6):
    if sayı%2==0:
        continue
    print(sayı)
    
#Pass;
for sayı in range(1,6):
    if sayı%2==0:
        pass
    else:
        print(sayı)