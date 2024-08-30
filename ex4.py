# Importando modulo de Teste
import unittest

def add(a,b):
    return max(a, b)

# Criando Classe que será usada para organizar e executar os testes
class TestAddFunction(unittest.TestCase):
    # Método de Teste (Devem começar com test_)
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 3) # self.assertEqual(A, B) - Verifica se A é igual a B

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 3)

# Executar os Testes
if __name__ == '__main__': # Executa apenas quando o script é executado diretamente
    unittest.main()