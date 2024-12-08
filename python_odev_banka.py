"""
  Proje Tanımı:
    Bir banka sistemi tasarlayın. Kullanıcı hesap açabilir, para yatırabilir,
    çekebilir ve bakiye kontrolü yapabilir.
  İstenilen Özellikler:
    Kullanıcıların hesap açması (ad, hesap numarası, başlangıç bakiyesi ile).
    Para yatırma ve çekme işlemleri.
    Hesap bakiyesi sorgulama.
    Birden fazla kullanıcıyı yönetebilme.
  Yönerge:
    Kullanici adında bir sınıf oluşturun. Bu sınıf, hesap numarasını ve
    bakiyeyi tutar.
    Banka adında bir sınıf oluşturun. Bu sınıf, kullanıcıların oluşturulmasını
    ve işlemlerinin yapılmasını sağlar.
    Giriş kontrolü (hesap numarasına göre) ve para çekme işleminde bakiye
    kontrolü ekleyin.
"""

class Kullanici:
    def __init__(self, ad, hesap_numarasi, baslangic_bakiyesi=0):
        self.ad = ad
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = baslangic_bakiyesi

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL hesabınıza yatırıldı. Yeni bakiyeniz: {self.bakiye} TL")
        else:
            print("Geçersiz para yatırma miktarı.")

    def para_cek(self, miktar):
        if 0 < miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL hesabınızdan çekildi. Yeni bakiyeniz: {self.bakiye} TL")
        else:
            print("Yetersiz bakiye veya geçersiz çekme miktarı.")

    def bakiye_sorgula(self):
        print(f"Hesap bakiyeniz: {self.bakiye} TL")


class Banka:
    def __init__(self):
        self.kullanicilar = {}

    def hesap_ac(self, ad, hesap_numarasi, baslangic_bakiyesi=0):
        if hesap_numarasi not in self.kullanicilar:
            kullanici = Kullanici(ad, hesap_numarasi, baslangic_bakiyesi)
            self.kullanicilar[hesap_numarasi] = kullanici
            print(f"{ad} adlı kullanıcı için {hesap_numarasi} numaralı hesap oluşturuldu.")
        else:
            print("Bu hesap numarası zaten mevcut.")

    def giris_yap(self, hesap_numarasi):
      if hesap_numarasi in self.kullanicilar:
        return self.kullanicilar[hesap_numarasi]
      else:
        print("Geçersiz hesap numarası")
        return None

    def islem_yap(self, kullanici):
      if kullanici:
        while True:
          print("\nİşlem Seçiniz:")
          print("1. Para Yatır")
          print("2. Para Çek")
          print("3. Bakiye Sorgula")
          print("4. Çıkış")

          secim = input("Seçiminiz: ")

          if secim == "1":
              miktar = float(input("Yatırılacak miktarı girin: "))
              kullanici.para_yatir(miktar)
          elif secim == "2":
              miktar = float(input("Çekilecek miktarı girin: "))
              kullanici.para_cek(miktar)
          elif secim == "3":
              kullanici.bakiye_sorgula()
          elif secim == "4":
              break
          else:
              print("Geçersiz işlem seçimi.")
      else:
        pass #Hata mesajı zaten giris_yap fonksiyonunda veriliyor.


# Örnek kullanım
banka = Banka()
banka.hesap_ac("Ali", "12345", 1000)
banka.hesap_ac("Ayşe", "67890")

giris_hesap_no = input("Hesap numaranızı giriniz: ")

giris_yapan_kullanici = banka.giris_yap(giris_hesap_no)

banka.islem_yap(giris_yapan_kullanici)
     