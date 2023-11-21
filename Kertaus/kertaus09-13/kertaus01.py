class Eläin:
    # Konstruktori
    def __init__(self, tyyppi, ääni):
        self.tyyppi = tyyppi
        self.ääni = ääni

    # Luokan metodi
    def tee_ääni(self):
        print(f"{self.tyyppi} {self.ääni}")
        return


# Luodaan olio
eläin1 = Eläin("leijona", "karjuu")
eläin2 = Eläin("tiikeri", "murisee")
# Käytetään luokan metodia
eläin1.tee_ääni()
eläin2.tee_ääni()
