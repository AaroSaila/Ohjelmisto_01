class Hissi:
    def __init__(self):
        self.kerros = 1
        self.ylin = 10
        self.alin = 1

    def kerros_ylos(self):
        self.kerros += 1
        if self.kerros > self.ylin:
            self.kerros = self.ylin
        result = "Hissi on " + str(self.kerros) + ". kerroksessa"
        return result

    def kerros_alas(self):
        self.kerros -= 1
        if self.kerros < self.alin:
            self.kerros = self.alin
        result = "Hissi on " + str(self.kerros) + ". kerroksessa"
        return result

    def siirry_kerrokseen(self, kerros):
        while self.kerros < kerros:
            self.kerros_ylos()
        while self.kerros > kerros:
            self.kerros_alas()
        return
