import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from io import StringIO
from app.views import exibir_pagina_pesquisa_eventos
from app.controllers import registrar_novo_evento

class TestEventSearch(unittest.TestCase):
    def setUp(self):
        registrar_novo_evento("teste", "teste", "01/01/2024", "12:45", "teste", "https://imagemteste.jpeg", "DescricaoTeste")

    @patch("builtins.input", side_effect=["", "teste", ""])
    def test_find_event_by_category_sucess(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_pesquisa_eventos()
            output = mock_stdout.getvalue().strip()
        self.assertIn("- teste (01/01/2024, 12:45, teste)", output)

    @patch("builtins.input", side_effect=["", "NovaCategoria", ""])
    def test_find_event_by_category_in_empty_category(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            exibir_pagina_pesquisa_eventos()
            output = mock_stdout.getvalue().strip()
        self.assertIn("Nenhum evento encontrado para os filtros selecionados.", output)

if __name__ == '__main__':
    unittest.main()
