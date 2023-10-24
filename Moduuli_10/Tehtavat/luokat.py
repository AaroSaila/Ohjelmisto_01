class Hissi:
    def __init__(self, alin, ylin):
        self.kerros = alin
        self.ylin = ylin
        self.alin = alin
        return

    def kerros_ylos(self):
        self.kerros += 1
        if self.kerros > self.ylin:
            self.kerros = self.ylin
        print("Hissi on " + str(self.kerros) + ". kerroksessa")
        return

    def kerros_alas(self):
        self.kerros -= 1
        if self.kerros < self.alin:
            self.kerros = self.alin
        print("Hissi on " + str(self.kerros) + ". kerroksessa")
        return

    def siirry_kerrokseen(self, kerros):
        while self.kerros < kerros:
            self.kerros_ylos()
        while self.kerros > kerros:
            self.kerros_alas()
        return


class Talo:

    def __init__(self, alin, ylin, hissit_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissit_lkm):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)
        return

    def aja_hissia(self, hissin_nmro, kohdekerros):
        Hissi.siirry_kerrokseen(self.hissit[hissin_nmro], kohdekerros)
        return

    def palohalytys(self):
        for i in range(len(self.hissit)):
            self.aja_hissia(i, self.alin)
        return
