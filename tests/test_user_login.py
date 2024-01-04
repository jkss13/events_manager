import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from io import StringIO
from app.views import exibir_pagina_login
from app.controllers import registrar_novo_usuario

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        registrar_novo_usuario(1, 'Teste', '123456789', 'teste@gmail.com', 'Senha123!')

    @patch('builtins.input', side_effect=['teste@gmail.com', 'Senha123!', 'N', '2'])
    def test_realizar_login_com_sucesso(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_login()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Login realizado com sucesso!", output)

    @patch('builtins.input', side_effect=['teste@gmail.com', 'SenhaErrada'])
    def test_realizar_login_com_email_ou_senha_incorretos(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_login()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Email ou senha incorretos.", output)

    @patch('builtins.input', side_effect=['email_inexistente@gmail.com', 'Senha123!', 'N'])
    def test_tentar_realizar_login_sem_cadastro(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_login()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Não há perfil cadastrado com o e-mail informado.", output)

    @patch('builtins.input', side_effect=['teste@gmail.com', 'Senha123!', 'S', '2'])
    def test_realizar_login_e_salvar_dados_de_login(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_login()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Login salvo com sucesso!", output)

if __name__ == '__main__':
    unittest.main()
