import os
import pytest
from unittest.mock import patch
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from src.preprocessing.taxi_data_processor import TaxiDataProcessor
from src.utils.config import HADOOP, JDBC_DRIVER_PATH

@pytest.fixture(scope="module")
def spark():
    os.environ["HADOOP_HOME"] = HADOOP
    os.environ["PATH"] += os.pathsep + os.path.join(HADOOP, "bin")
    return SparkSession.builder \
        .appName("TestProcessor") \
        .config("spark.jars", JDBC_DRIVER_PATH) \
        .getOrCreate()

@patch("src.preprocessing.taxi_data_processor.SparkSession.read", create=True)
def test_tratar_dados_with_mock(mock_read, spark):
    # Define schema manualmente
    schema = StructType([
        StructField("VendorID", IntegerType(), True),
        StructField("tpep_pickup_datetime", StringType(), True),
        StructField("tpep_dropoff_datetime", StringType(), True),
        StructField("passenger_count", IntegerType(), True),
        StructField("trip_distance", StringType(), True),
        StructField("RatecodeID", IntegerType(), True),
        StructField("PULocationID", IntegerType(), True),
        StructField("DOLocationID", IntegerType(), True),
        StructField("payment_type", IntegerType(), True),
        StructField("fare_amount", FloatType(), True),
        StructField("extra", FloatType(), True),
        StructField("mta_tax", FloatType(), True),
        StructField("tip_amount", FloatType(), True),
        StructField("tolls_amount", FloatType(), True),
        StructField("improvement_surcharge", FloatType(), True),
        StructField("total_amount", FloatType(), True),
        StructField("congestion_surcharge", FloatType(), True),
        StructField("store_and_fwd_flag", StringType(), True),
        StructField("Airport_fee", FloatType(), True),
        StructField("cbd_congestion_fee", FloatType(), True),
    ])

    # Dados simulados
    data = [(
        1, "2023-01-01 10:00:00", "2023-01-01 10:15:00", None, "2.5", 1, 132, 236, 1,
        None, 0.5, 0.5, None, 0.0, 0.3, None, 2.75, "N", 0.0, 0.0
    )]

    mock_df = spark.createDataFrame(data, schema=schema)
    mock_read.parquet.return_value = mock_df

    processor = TaxiDataProcessor(parquet_path="fake_path", spark=spark)
    processor.carregar_dados()
    processor.tratar_dados()

    # Verifica colunas esperadas após tratamento
    expected_cols = [
        "VendorID", "pickup_datetime", "dropoff_datetime", "passenger_count",
        "trip_distance", "RatecodeID", "PULocationID", "DOLocationID",
        "payment_type", "fare_amount", "extra", "mta_tax", "tip_amount",
        "tolls_amount", "improvement_surcharge", "total_amount",
        "congestion_surcharge", "trip_duration", "last_updated", "pickup_date"
    ]

    assert processor.df is not None
    assert all(col in processor.df.columns for col in expected_cols)
    assert "store_and_fwd_flag" not in processor.df.columns
    assert "Airport_fee" not in processor.df.columns
    assert "cbd_congestion_fee" not in processor.df.columns
