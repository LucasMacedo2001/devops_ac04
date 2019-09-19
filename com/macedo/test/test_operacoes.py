from unittest import TestCase
from com.macedo.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_Por3(self):
		self.assertEqual(self.operacoes.multiplicacaoPor3([1,5]), 15, "Should be 15")
		
	def test_Por7(self):
		self.assertEqual(self.operacoes.multiplicacaoPor7([1,4]), 28, "Should be 28")