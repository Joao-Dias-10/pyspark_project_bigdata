import pytest
from src.utils.parquet_helper import ParquetHelper

def test_localiza_arquivo_parquet(tmp_path):
    # Cria um falso arquivo .parquet
    fake_file = tmp_path / "part-00000.parquet"
    fake_file.write_text("conteúdo fake")
    
    path_resultado = ParquetHelper.localizar_arquivo_parquet(str(tmp_path))
    assert path_resultado.endswith(".parquet")
    assert "part-00000.parquet" in path_resultado

def test_erro_arquivo_parquet_nao_encontrado(tmp_path):
    with pytest.raises(FileNotFoundError):
        ParquetHelper.localizar_arquivo_parquet(str(tmp_path))
