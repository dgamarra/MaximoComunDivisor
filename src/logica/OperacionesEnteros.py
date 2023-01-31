class OperacionesEnteros:

    def MCD(self, numero1, numero2):
        temporal = 0

        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1

    def MCD3(self, numero1, numero2, numero3):
        numero1 = self.MCD(numero1, numero2)
        numero1=self.MCD(numero1, numero3)
        return numero1