import os
import tempfile
import pytest
from unittest.mock import patch, MagicMock
from src.automation.downloads import Downloads

@patch("src.automation.downloads.requests.get")
def test_download_file(mock_get):
    # Simula resposta da requisição
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = b"arquivo-falso"
    mock_get.return_value = mock_response

    # Cria diretório temporário para testes
    with tempfile.TemporaryDirectory() as tmpdir:
        downloader = Downloads(path_raw=tmpdir)
        file_name = "teste.parquet"
        test_url = "http://fake-url.com/teste.parquet"

        result_path = downloader.download_file(test_url, file_name)

        # Verifica se o arquivo foi salvo no caminho esperado
        assert os.path.exists(result_path)
        assert result_path.endswith(file_name)

        # Verifica conteúdo escrito no arquivo
        with open(result_path, "rb") as f:
            content = f.read()
        assert content == b"arquivo-falso"

        # Verifica se requests.get foi chamado corretamente
        mock_get.assert_called_once_with(test_url)
