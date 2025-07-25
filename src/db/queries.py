from pyspark.sql import SparkSession
from src.utils.config import COLUMN_RENAME_MAP 

class Inserter:
    def __init__(self, jdbc_url: str, properties: dict, jdbc_driver_path: str):
        self.jdbc_url = jdbc_url
        self.properties = properties
        self.spark = None
        self.jdbc_driver_path = jdbc_driver_path

    def __enter__(self):
        self.spark = SparkSession.builder \
            .appName("InsercaoBanco") \
            .config("spark.jars", self.jdbc_driver_path) \
            .getOrCreate()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.spark:
            self.spark.stop()

    def insert(self, parquet_path: str, table_name: str, mode: str = "append") -> None:
        df = self.spark.read.parquet(parquet_path)

        # Necessário. Renomeia colunas do '.parquet' para ter os mesmos nomes das col do banco.
        for old_col, new_col in COLUMN_RENAME_MAP().items():
            if old_col in df.columns:
                df = df.withColumnRenamed(old_col, new_col)

        df.write.jdbc(
            url=self.jdbc_url,
            table=table_name,
            mode=mode,
            properties=self.properties
        )
