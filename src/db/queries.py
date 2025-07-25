from pyspark.sql import SparkSession
from src.utils.config import COLUMN_RENAME_MAP 

class Inserter:
    def __init__(self, spark: SparkSession, jdbc_url: str, properties: dict, jdbc_driver_path: str):
        self.spark = spark
        self.jdbc_url = jdbc_url
        self.properties = properties
        self.jdbc_driver_path = jdbc_driver_path

    def insert(self, parquet_path: str, table_name: str, mode: str = "append") -> None:
        df = self.spark.read.parquet(parquet_path)

        for old_col, new_col in COLUMN_RENAME_MAP().items():
            if old_col in df.columns:
                df = df.withColumnRenamed(old_col, new_col)

        df.write.option("numPartitions", 4).option("batchsize", 1000).jdbc(
            url=self.jdbc_url,
            table=table_name,
            mode=mode,
            properties=self.properties
        )
