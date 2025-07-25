import pytest
from unittest.mock import MagicMock, patch
from src.db.queries import Inserter


@pytest.fixture
def fake_spark():
    # Simula um DataFrame com colunas para renomear
    df_mock = MagicMock()
    df_mock.columns = ['VendorID', 'RatecodeID']
    df_mock.withColumnRenamed.side_effect = lambda old, new: df_mock
    df_mock.write.option.return_value = df_mock.write
    df_mock.write.jdbc = MagicMock()

    spark = MagicMock()
    spark.read.parquet.return_value = df_mock
    return spark


@patch("src.db.queries.COLUMN_RENAME_MAP")
def test_inserter_insert_renames_and_writes(mock_column_map, fake_spark):
    # Simula o map de renomeação de colunas
    mock_column_map.return_value = {
        "VendorID": "vendor_id",
        "RatecodeID": "ratecode_id"
    }

    inserter = Inserter(
        spark=fake_spark,
        jdbc_url="jdbc:fake",
        properties={"user": "test", "password": "123"},
        jdbc_driver_path="/caminho/falso/driver.jar"
    )

    parquet_path = "/caminho/falso/dados.parquet"
    table_name = "tabela_teste"

    inserter.insert(parquet_path, table_name)

    # Verifica se o parquet foi lido
    fake_spark.read.parquet.assert_called_once_with(parquet_path)

    # Verifica se as colunas foram renomeadas
    df_mock = fake_spark.read.parquet.return_value
    df_mock.withColumnRenamed.assert_any_call("VendorID", "vendor_id")
    df_mock.withColumnRenamed.assert_any_call("RatecodeID", "ratecode_id")

    # Verifica se foi chamada a escrita no JDBC
    df_mock.write.option.assert_any_call("numPartitions", 4)
    df_mock.write.option.assert_any_call("batchsize", 1000)
    df_mock.write.jdbc.assert_called_once_with(
        url="jdbc:fake",
        table=table_name,
        mode="append",
        properties={"user": "test", "password": "123"}
    )
