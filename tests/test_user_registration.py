import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from io import StringIO
from app.views import exibir_pagina_registro_usuario

class TestUserRegistration(unittest.TestCase):
    @patch("builtins.input", side_effect=["1", "Fulano", "123456789", "fulano@gmail.com", "Senha123!", "N"])
    def test_register_common_profile_success(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_registro_usuario()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Usuário Fulano registrado com sucesso!", output)

    @patch("builtins.input", side_effect=["1", "Ciclano", "987654321", "fulano@gmail.com", "Senha123!", "N"])
    def test_register_profile_with_existing_email(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_registro_usuario()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Já existe um cadastro com o e-mail fulano@gmail.com.", output)

    @patch("builtins.input", side_effect=["1", "Beltrano", "111111111", "beltrano@gmail.com", "123", "Senha123!", "N"])
    def test_register_profile_with_invalid_password(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_registro_usuario()
            output = mock_stdout.getvalue().strip()
        self.assertIn("A senha não atende aos requisitos de segurança.", output)

if __name__ == "__main__":
    unittest.main()

