import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from io import StringIO
from app.views import exibir_pagina_registro_evento
from app.controllers import registrar_novo_evento

class TestEventRegistration(unittest.TestCase):
    def setUp(self):
        registrar_novo_evento("EventoExistente", "CategoriaTeste", "01/01/2024", "12:45", "LocalTeste", "https://imagemteste.jpeg", "DescricaoTeste")

    @patch("builtins.input", side_effect=["TituloTeste", "CategoriaTeste", "01/01/2024", "12:45", "LocalTeste", "https://imagemteste.jpeg", "DescricaoTeste"])
    def test_register_event_success(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_registro_evento()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Evento TituloTeste registrado com sucesso!", output)

    @patch("builtins.input", side_effect=["EventoExistente", "CategoriaTeste", "01/01/2024", "12:45", "LocalTeste", "https://imagemteste.jpeg", ""])
    def test_register_event_with_exist_title(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_registro_evento()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Já existe um evento com o título EventoExistente. Escolha um nome diferente.", output)

    @patch("builtins.input", side_effect=["", "CategoriaTeste", "01/01/2024", "12:45", "LocalTeste", "https://imagemteste.jpeg", "DescricaoTeste"])
    def test_register_event_without_fill_required_fields(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_registro_evento()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Todos os campos obrigatórios devem ser preenchidos para concluir o cadastro.", output)

    @patch("builtins.input", side_effect=["OutroTeste", "CategoriaTeste", "01/01/2024", "12:45", "LocalTeste", "", ""])
    def test_register_event_without_fill_image(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_registro_evento()
            output = mock_stdout.getvalue().strip()
        self.assertIn("É necessário fornecer o caminho da imagem para concluir o cadastro.", output)

if __name__ == '__main__':
    unittest.main()
