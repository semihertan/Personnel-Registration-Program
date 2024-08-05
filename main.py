from prettytable import PrettyTable

class Kimlik:
    def __init__(self, tc_no, ad, soyad, dogum_tarihi):
        self.tc_no = tc_no
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi

class Personel(Kimlik):
    def __init__(self, tc_no, ad, soyad, dogum_tarihi, departman, giris_tarihi, maas):
        super().__init__(tc_no, ad, soyad, dogum_tarihi)
        self.departman = departman
        self.giris_tarihi = giris_tarihi
        self.maas = maas

    def __str__(self):
        return f"TC NO: {self.tc_no}\nADI: {self.ad}\nSOYAD: {self.soyad}\nDEPARTMAN: {self.departman}\nİŞE GİRİŞ TARİHİ: {self.giris_tarihi}\nMAAŞ: {self.maas}"

    def id_olustur(self):
        id_ad = self.ad[:2]
        id_departman = self.departman[-2:]
        id_giris_tarihi = self.giris_tarihi.split('/')[0] + self.giris_tarihi.split('/')[1]
        return id_ad + id_departman + id_giris_tarihi

def main():
    girilen_personel_sayisi = 0
    toplam_maas = 0
    departmanlar = {
        "satış": [],
        "finans": [],
        "insan kaynakları": [],
        "pazarlama": []
    }
    departman_istatistikleri = {}

    while True:
        tc_no = input("TC KİMLİK NUMARASI: ")
        ad = input("ADI: ")
        soyad = input("SOYADI: ")
        dogum_tarihi = input("DOĞUM TARİHİ (GG/AA/YYYY): ")
        departman = input("DEPARTMAN (SATIŞ-FİNANS-İNSAN KAYNAKLARI-PAZARLAMA): ")
        giris_tarihi = input("GİRİŞ TARİHİ (GG/AA/YYYY): ")
        maas = float(input("MAAŞ: "))

        personel = Personel(tc_no, ad, soyad, dogum_tarihi, departman, giris_tarihi, maas)
        departmanlar[departman.lower()].append(personel)

        toplam_maas += maas
        girilen_personel_sayisi += 1
        ort_maas = toplam_maas / girilen_personel_sayisi

        print("-----------------------------------------------------")
        print("GİRİLEN PERSONELİN BİLGİLERİ")
        print("-----------------------------------------------------")
        print(personel)
        print("-----------------------------------------------------")
        personel_kimlik = personel.id_olustur()
        print("-----------------------------------------------------")
        print(f"PERSONEL ID: {personel_kimlik}")
        print("-----------------------------------------------------")

        secim = input("PERSONEL KAYITTAN ÇIKMAK İÇİN (H) GİRİN: ")
        print("-----------------------------------------------------")
        secim = secim.upper()
        if secim == "H":
            break

    for departman, personeller in departmanlar.items():
        if personeller:
            toplam_maas_departman = sum(personel.maas for personel in personeller)
            personel_sayisi_departman = len(personeller)
            en_yuksek_maas_departman = max(personel.maas for personel in personeller)
            en_dusuk_maas_departman = min(personel.maas for personel in personeller)

            departman_istatistikleri[departman] = {
                "toplam_maas": toplam_maas_departman,
                "personel_sayisi": personel_sayisi_departman,
                "en_yuksek_maas": en_yuksek_maas_departman,
                "en_dusuk_maas": en_dusuk_maas_departman
            }
        else:
            departman_istatistikleri[departman] = {
                "toplam_maas": 0,
                "personel_sayisi": 0,
                "en_yuksek_maas": 0,
                "en_dusuk_maas": 0
            }

    # Personel Listesi Tablosu
    table_personel = PrettyTable()
    table_personel.field_names = ["DEPARTMAN", "ADI", "SOYADI", "GİRİŞ TARİHİ", "MAAŞ"]
    for departman, personeller in departmanlar.items():
        for personel in personeller:
            table_personel.add_row([
                departman.capitalize(),
                personel.ad,
                personel.soyad,
                personel.giris_tarihi,
                personel.maas
            ])

    print("\n+-----------+---------PERSONEL LİSTESİ----------+---------+")
    print(table_personel)

    # Departman İstatistikleri Tablosu
    table_istatistik = PrettyTable()
    table_istatistik.field_names = ["Departman", "Toplam Maaş", "Personel Sayısı", "En Yüksek Maaş", "En Düşük Maaş"]
    for departman, istatistikler in departman_istatistikleri.items():
        table_istatistik.add_row([
            departman.capitalize(),
            istatistikler['toplam_maas'],
            istatistikler['personel_sayisi'],
            istatistikler['en_yuksek_maas'],
            istatistikler['en_dusuk_maas']
        ])

    print("\n+------------------+------------DEPARTMAN İSTATİSTİKLERİ-------------+---------------+")
    print(table_istatistik)


    table_sirket = PrettyTable()
    table_sirket.field_names = ["Toplam Maaş", "Ortalama Maaş"]

    table_sirket.add_row([
        toplam_maas,
        ort_maas
    ])

    print("\n----------- ŞİRKET TOPLAM MAAŞ BİLGİLERİ -----------")
    print(table_sirket)

if __name__ == "__main__":
    main()
