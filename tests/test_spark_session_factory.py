from unittest.mock import patch, MagicMock
from src.utils.spark_session_factory import SparkSessionFactory


@patch("src.utils.spark_session_factory.SparkSession")
def test_create_spark_session(mock_spark_cls):
    # Cria mocks encadeados
    builder_mock = MagicMock()
    spark_instance_mock = MagicMock()

    # Encadeamento .appName().config().getOrCreate()
    builder_mock.appName.return_value = builder_mock
    builder_mock.config.return_value = builder_mock
    builder_mock.getOrCreate.return_value = spark_instance_mock

    mock_spark_cls.builder = builder_mock

    factory = SparkSessionFactory(app_name="teste")
    spark = factory.create()

    assert spark == spark_instance_mock
    builder_mock.appName.assert_called_with("teste")

    # Verifica que config foi chamado com "spark.jars"
    args, _ = builder_mock.config.call_args
    assert args[0] == "spark.jars"
