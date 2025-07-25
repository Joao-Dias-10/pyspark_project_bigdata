import pytest
from sqlalchemy import inspect, create_engine
from src.db.models import Base


def test_tables_created():
    # Usa SQLite em memória só para o teste
    test_engine = create_engine("sqlite:///:memory:")

    # Cria as tabelas usando os modelos
    Base.metadata.create_all(test_engine)

    # Inspeciona se as tabelas foram criadas no banco
    inspector = inspect(test_engine)
    tables = inspector.get_table_names()

    # Espera que tenha pelo menos uma tabela definida no modelo
    assert len(tables) > 0, "Nenhuma tabela foi criada no banco"

