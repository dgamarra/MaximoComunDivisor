class OperacionesEnteros:
    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1

    def MCD3(self, numero1, numero2, numero3):
        temporal = self.MCD(numero1, numero2)
        temporal = self.MCD(numero3,temporal)
        return temporal