class Insan:
    def __init__(self, boy, kilo, grengi, suzun, srengi, yas, cinsiyet, isim, soyad):
        self.boy = boy
        self.kilo = kilo
        self.grengi = grengi
        self.suzun = suzun
        self.srengi = srengi
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.isim = isim
        self.soyad = soyad

    def isimDegistir(self, yeni_isim):
        self.isim = yeni_isim

    def kisiyiOzetGec(self):
        print("Merhaba ben " + self.isim + ". " + str(self.yas) + " yaşındayım.")

    def boylariKarsilastır(self, baska_bir_insan):
        if self.boy > baska_bir_insan.boy:
            print(self.isim + " daha uzun")
        else:
            print(baska_bir_insan.isim + " daha uzun")


insan_bir = Insan(1.77, 67, "kahverengi", "uzun", "kahvrengi", 18, "kız", "Nehir", "Arık")
insan_iki = Insan(1.60, 51, "kahverengi", "orta", "kahverengi", 20, "kız", "Zehra", "Usta")

print(insan_bir.isim)
insan_bir.isimDegistir("Yakamoz")
print(insan_bir.isim)
print(insan_iki.isim)
insan_iki.isimDegistir("Sen Bul")
print(insan_iki.isim)
insan_bir.boylariKarsilastır(insan_iki)
insan_iki.boylariKarsilastır(insan_bir)
