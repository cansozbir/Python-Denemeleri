import random
class Bilgisayar():
    def __init__(self,pc_durum="Kapalı",pc_ses=0,ram_miktari=8,isletim_sistemi="Linux"):
        self.pc_durum=pc_durum
        self.pc_ses=pc_ses
        self.ram_miktari=ram_miktari
        self.isletim_sistemi=isletim_sistemi

    def sesi_azalt_arttir(self):
        while True :
            karakter =input("\nAzaltmak istiyorsan '<' , acmak istiyorsan '>' , if it's ok press q ")
            if karakter=="<" :
                if self.pc_ses > 0 :
                    self.pc_ses -= 1
                    print("\nSes: ",self.pc_ses)
            elif karakter==">":
                if self.pc_ses<100 :
                    self.pc_ses += 1
                    print ("\nSes: ",self.pc_ses)
            else :
                print("\nSes güncellendi: ",self.pc_ses)
                break

    def pc_kapat(self):
        if self.pc_durum=="Açık\n" :
            print("pc kapatılıyor...")
            self.pc_durum="Kapalı\n"
        else :
            print("Cihaz zaten Kapalı...")
    
    def pc_ac(self):
        if self.pc_durum=="Kapalı" :
            print("pc açılıyor...\n")
            self.pc_durum="Açık"
        else :
            print("Cihaz zaten Açık...\n")
    
    def upgrade_ram(self):
        x=random.randint(1,8)
        if self.ram_miktari <32:
            self.ram_miktari += x
        print("Yeni ram miktariniz: ",self.ram_miktari)

    def bilgiler(self):
        print("\n\n\n\n Bilgisayarın durumu: {}\nSes seviyesi: {}\nRam miktari: {}, isletim sistemi: {}\n\n\n\n".format(self.pc_durum,self.pc_ses,self.ram_miktari,self.isletim_sistemi))
    
    def isletimidegistir(self):
        if self.isletim_sistemi == "Linux" :
            self.isletim_sistemi = "Windows"
        elif self.isletim_sistemi == "Windows":
            self.isletim_sistemi = "Linux"
        print ("\n\nŞuanki işletim sisteminiz {} olarak guncellendi\n\n ".format (self.isletim_sistemi))





dellinspiron = Bilgisayar()
print( """\n\n\n********************

Bilgisayar Uygulamasi
İşlemler ;

1. Pc yi aç

2. Pc yi kapat

3. Ram miktarini arttir 

4. İşletim sistemini degistir

5. sistem özelliklerini goster 

6. çıkmak için q ya basiniz
************************\n\n\n""")

while True :
    işlem = input("işleminizi seçiniz: ")
    if (işlem=="q"):
        exit()
    elif işlem =="1" :
        dellinspiron.pc_ac()
    elif işlem=="2" :
        dellinspiron.pc_kapat()
    elif işlem=="3" :
        dellinspiron.upgrade_ram()
    elif işlem=="4":
        dellinspiron.isletimidegistir()    
    elif  işlem=="5":
        dellinspiron.bilgiler()
    else :
        print ("\n\n\ngeçersiz işlem!") 

