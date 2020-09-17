from unittest import TestCase
from OO.carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)