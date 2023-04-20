import unittest
from src.OperacionesEnteros import OperacionesEnteros

class PruebaOperacionesEnteros(unittest.TestCase):
    def setUp(self):
        self.operacion = OperacionesEnteros()
    def tearDown(self):
        self.operacion = None
    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6

        # Do
        resultadoActual = self.operacion.MCD(numero1, numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_tresNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 24679
        numero2 = 20387
        numero3 = 16169

        resultadoEsperado = 37

        # Do
        resultadoActual = self.operacion.MCD3(numero1, numero2, numero3)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)