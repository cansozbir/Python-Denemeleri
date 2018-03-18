class universite:
    def __init__(self,universite_adi,universite_tipi,ogrsayisi,hocasayisi,sinifsayisi):
        self.universite_adi=universite_adi
        self.universite_tipi=universite_tipi
        self.ogrsayisi=ogrsayisi
        self.hocasayisi=hocasayisi
        self.sinifsayisi=sinifsayisi
        self.ogrenciler=[]
    
    def bilgileriyaz(self):
        print("\n\nuniversite adi: {}\n\nuniversite tipi: {}\n\nogrencisayisi: {}\n\nogretmensayisi: {}\n\nsınıf sayısı: {}\n\n\n".format(self.universite_adi,
            self.universite_tipi,self.ogrsayisi,self.hocasayisi,self.sinifsayisi))
    
        
    def tipdegistir(self):
        if self.universite_tipi=="Standart":
            self.universite_tipi="Teknik"
        else:
            self.universite_tipi="Standart"
        print("\n\nUniversite tipiniz {} olarak guncellenmistir...\n\n".format(self.universite_tipi))
    
    
    def kayityap(self):
        print("eklenecek ogrencilerin tamami yazildiginda q yaziniz")
        while True:
            x=input("\n\nisim soyisim giriniz: ")
            if x!="q":
              if x not in self.ogrenciler :  
                 self.ogrenciler.append(x)
                 print ("\n",x, "basariyla kaydedilmistir")
                 self.ogrsayisi += 1
            else:
                print("\n\nGuncel ogrenci sayisi {} dir ".format(self.ogrsayisi))
                break
    
    def kisalt(self):
        liste=self.universite_adi.split(" ")
        kisaltmasi=""
        for i in liste:
            kisaltmasi += i[0]
        # kisaltmasi = kisaltmasi.upper()
        print("\n\nUniversiteniz için en uygun kısaltma :",kisaltmasi)


a=input("Üniversite ismi: ")
b=input("Tipi: ")
c=int(input("Öğrenci sayisi: "))
d=int(input("Öğretmen sayisi: "))
e=int(input("Sinif sayisi: "))

üniversite=universite(a,b,c,d,e)


while True :
    print(""" \nişlemler:
 1.Bilgileri Görüntüle
 2.Tip Değiştir
 3.Öğrenci Kaydı Yap
 4.Üniversiteye bir kısaltma bul
 çıkmak için q girebilirsin...\n
  """)

    işlem=input("Yapmak istediginiz işlem: ")
    if işlem =="q" :
        print ("Çıkış yapılıyor ..........")
        exit()
    elif işlem=="1":
        üniversite.bilgileriyaz()
    elif işlem=="2":
        üniversite.tipdegistir()
    elif işlem=="3":
        üniversite.kayityap()
    elif işlem=="4":
        üniversite.kisalt()

