    # -*- coding: utf-8 -*-
# MODÜLLER 
# os modülü klasörler dosyalar hakkında bizlere yardımcı olur.
import os

# Kullanmış olduğun dosyanın yerini gösterir.
print(os.getcwd())
print()

# Olduğu klasörün içindekileri listeler.
print(os.listdir())
print()

# Bu şekilde de farklı bir klasörün içindekileri bastırmak için kullanılabilir.
print(os.listdir("C:\\Users"))
print()

# Alttaki komut şuan ki kullanmış olduğun dosyayı içine yazdığın yere taşır.
"""
os.chdir()

"""

# Bir örnek kullanım:
dosyalar = os.listdir()
for eleman in dosyalar:
    print("--  " + eleman)
    
# Bu komut istediğin konumda sana o adlı klasörü oluşturur.
'''

os.mkdir("C:\\Users\Fatih\Documents\Okul\Murat Yazılım\Pratiklerim\\Modül deneme 1")

'''

# Bu komut o konumdaki klasörü siler.
# Fakat klasörün içinde bir şeyler varsa hata alınabilir o yüzden silerken içini boş tutmaya gayret et.
'''

os.rmdir("C:\\Users\Fatih\Documents\Okul\Murat Yazılım\Pratiklerim\\Modül deneme 1")

'''

## os.O_RDONLY - Read Only      - Sadece Oku
## os.O_WRONLY - Write Only     - Sadece Yaz
## os.O_RDWR   - Read and Write - Oku ve Yaz
## os.O_CREAT  - Create         - Oluştur


# Burda yeni txt dosyası oluşturup özelliklerini atadık.
# Encode str yi bite cinsine çevirdi ama ü gibi özel karakterlerde sıkıntı çıkarabiliyor.
# En sonunda dosyayı kapattık ve oluşturmuş olduk.

'''

yeni_dosya = os.open("yeni_dosya.txt", os.O_RDWR |os.O_CREAT)
os.write(yeni_dosya, "Merhaba Dünya!".encode())
os.close(yeni_dosya)

'''

# İçeriğini yazdırmak.

'''

yeni_dosya = os.open("yeni_dosya.txt", os.O_RDONLY)
uzunluk = os.stat(yeni_dosya).st_size
içerik = os.read(yeni_dosya, uzunluk)
print(içerik.decode())
os.close(yeni_dosya)

'''

# Dosya silmek için unlink kullanılır.

'''

os.ulink("yeni_dosya.txt")

'''

# Klasörün adını değiştirmek.
# denemeye yeni adlı klasörün adı artık deneme eski oldu.

'''

os.rename("deneme_yeni", "deneme_eski")

'''

