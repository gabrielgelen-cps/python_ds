# Importando modulo de Teste
import unittest

def add(a,b,c):
    return a + b + c

# Criando Classe que será usada para organizar e executar os testes
class TestAddFunction(unittest.TestCase):
    # Método de Teste (Devem começar com test_)
    def test_add_nome(self):
        self.assertEqual(add('Meu nome ', 'é ', 'Gabriel'), 'Meu nome é Gabriel') # self.assertEqual(A, B) - Verifica se A é igual a B

# Executar os Testes
if __name__ == '__main__': # Executa apenas quando o script é executado diretamente
    unittest.main()