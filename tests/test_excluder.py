import os
from pathlib import Path
from src.utils.excluder import Excluder

def test_clear_contents(tmp_path):
    # Cria arquivos e subpastas
    (tmp_path / "arquivo.txt").write_text("teste")
    sub_dir = tmp_path / "subdir"
    sub_dir.mkdir()
    (sub_dir / "arquivo2.txt").write_text("teste")

    excluder = Excluder(str(tmp_path))
    excluder.clear_contents()

    assert not any(tmp_path.iterdir())  # diretório deve estar vazio
