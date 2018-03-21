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

new_human = Insan(1.77, 67, "kahverengi", "uzun", "kahvrengi", 18, "kız", "Nehir", "Arık")

print(new_human.isim)
new_human.isimDegistir("Yakamoz")
print(new_human.isim)
print(new_human.kisiyiOzetGec())