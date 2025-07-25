import os
import pytest
from pyspark.sql import SparkSession
from src.preprocessing.taxi_data_processor import TaxiDataProcessor

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.master("local[*]").appName("Test").getOrCreate()

def test_taxi_data_processing(tmp_path, spark):
    # Arrange: cria DataFrame mock
    data = [
        (1, "2025-01-01 10:00:00", "2025-01-01 10:10:00", None, 1.5, 1, 101, 102, 1, 10.0, 0.5, 0.5, 2.0, 0.0, 0.3, 13.3, 2.5, 1.0, 1.0),
    ]
    columns = [
        "VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count", "trip_distance",
        "RatecodeID", "PULocationID", "DOLocationID", "payment_type", "fare_amount", "extra", "mta_tax",
        "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount", "congestion_surcharge",
        "Airport_fee", "cbd_congestion_fee"
    ]

    input_df = spark.createDataFrame(data, columns)
    input_path = tmp_path / "input.parquet"
    input_df.write.mode("overwrite").parquet(str(input_path))

    # Processa
    processor = TaxiDataProcessor(parquet_path=str(input_path))
    processor.carregar_dados()
    processor.tratar_dados()

    # Salva processado
    output_path = tmp_path / "processed"
    processor.salvar_dados_processados(str(output_path))
    
    # Assert
    assert os.path.exists(str(output_path))
    processed = spark.read.parquet(str(output_path))
    assert "trip_duration" in processed.columns
    assert "pickup_datetime" in processed.columns
    assert processed.count() == 1
    processor.encerrar()
