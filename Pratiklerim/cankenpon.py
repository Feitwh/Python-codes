#Taş Kağıt Makas Oyunu

import random

oyuncu = input("Seç(taş, kağıt veya makas bir tanesini seçiniz) :")
bilgisayar = random.choice(['taş','kağıt','makas'])

"taş > makas", "makas > kağıt", "kağıt > taş"
if oyuncu == bilgisayar:
    print("Berabere!!")
elif oyuncu > bilgisayar :
    print ("Tebrikler kazandınız!!")
else: 
    print("Kaybettiniz!")