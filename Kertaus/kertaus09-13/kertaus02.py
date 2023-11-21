# Lintu-luokka & aliluokat alkaa
class Eläin:
    def __init__(self, tyyppi, ääni):
        self.tyyppi = tyyppi
        self.ääni = ääni

    def tee_ääni(self):
        print(f"{self.tyyppi} {self.ääni}")
        return


class Lintu(Eläin):
    def __init__(self, tyyppi, ääni, väri):
        super().__init__(tyyppi, ääni)
        self.väri = väri
    
    # Metodien ylikirjoittaminen
    def tee_ääni(self):
        super().tee_ääni()
        print(f"Sulkieni väri on {self.väri}.")

#Lintu-luokka & aliluokat loppuu


class Eläintarha:
    def __init__(self):
        self.eläimet = []

    def lisää_eläin(self, eläin):
        self.eläimet.append(eläin)
        return
    
    def poista_eläin(self, eläin):
        self.eläimet.remove(eläin)
        return
    
    def listaa_eläimet(self):
        print("Tässä on kaikki eläintarhan eläimet ja niiden ääntäminen: ")
        for eläin in self.eläimet:
            eläin.tee_ääni()
        return


eläin1 = Eläin("leijona", "karjuu")
eläin2 = Eläin("tiikeri", "murisee")
lintu1 = Lintu("Käki", "Kukkuu", "Ruskea")

# Luodaan eläintarha
eläintarha = Eläintarha()
# Lisätään eläintarhaan eläin
eläintarha.lisää_eläin(eläin1)
eläintarha.lisää_eläin(lintu1)
eläintarha.lisää_eläin(eläin2)
eläintarha.listaa_eläimet()
