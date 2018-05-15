import random
import time


class tahtaolustur:
    def __init__(self):
        self.tahtadurumu=[["0","0","0"],["0","0","0"],["0","0","0"]]
        self.sira=random.randint(0,1)    
        self.kazanan="yok"

    def tahtagoster(self):
        if self.sira==0:
            print("Sizin hamleniz:\n")
        elif self.sira==1:
            print("Bilgisayarın hamlesi:\n")
        for i in range (3):
                print (self.tahtadurumu[i][0]+" "+self.tahtadurumu[i][1]+" "+self.tahtadurumu[i][2])
        print("\n")
    
    def winner(self):
        for i in range (3):
            if self.tahtadurumu[i][0]==self.tahtadurumu[i][1] and self.tahtadurumu[i][1]==self.tahtadurumu[i][2]:
                if self.tahtadurumu[i][0]=="X":
                    self.kazanan="Player"
                    break
                elif self.tahtadurumu[i][0]=="O":
                    self.kazanan="Computer"
                    break
            if self.tahtadurumu[0][i]==self.tahtadurumu[1][i] and self.tahtadurumu[1][i]==self.tahtadurumu[2][i]:
                if self.tahtadurumu[0][i]=="X":
                    self.kazanan="Player"
                    break
                elif self.tahtadurumu[0][i]=="O":
                    self.kazanan="Computer"
            if self.tahtadurumu[0][0]==self.tahtadurumu[1][1] and self.tahtadurumu[1][1]==self.tahtadurumu[2][2]:
                if self.tahtadurumu[0][0]=="X":
                    self.kazanan="Player"
                    break
                elif self.tahtadurumu[0][0]=="O":
                    self.kazanan="Computer"
                    break
            if self.tahtadurumu[0][2]==self.tahtadurumu[1][1] and self.tahtadurumu[1][1]==self.tahtadurumu[2][0]:
                if self.tahtadurumu[0][2]=="X":
                    self.kazanan="Player"
                    break
                elif self.tahtadurumu[0][2]=="O":
                    self.kazanan="Computer"
                    break
        if self.kazanan=="Player":
            print("\nTEBRIKLER KAZANDINIZ ＼(^o^)／")
        elif self.kazanan=="Computer":
            print("\nMAALESEF KAYBETTINIZ :( ")
        return self.kazanan

    def hamleyap(self):
        if self.sira==0:
            try:
                
                satir=int(input("Hamle yapmak istediginiz satir :"))
                sutun=int(input("Hamle yapmak istediginiz sutun :"))
            
                if (satir<1 or satir>3 or sutun<1 or sutun>3):
                    print("\ngecersiz aralık..")
                    self.hamleyap()

                if self.tahtadurumu[satir-1][sutun-1] != "0":
                    print("\ngecersiz hamle...")
                    self.hamleyap()
            
                self.tahtadurumu[satir-1][sutun-1]="X"
                self.tahtagoster()
                self.sira =self.sira+1
                self.winner()
            except:
                print("\nbilinmeyen bir hata olustu tekrar deneyiniz...\n")
                self.hamleyap()
        elif self.sira==1:
            time.sleep(0.5)
            satir=random.randint(0,2)
            sutun=random.randint(0,2)
            if self.tahtadurumu[satir][sutun]!="0":
                self.hamleyap()
            else:
                self.tahtadurumu[satir][sutun]="O"
                self.tahtagoster()
                self.winner()
                self.sira = self.sira -1
        


deneme=tahtaolustur()

while deneme.winner()=="yok":
    deneme.hamleyap()
   
