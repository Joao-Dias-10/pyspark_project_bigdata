import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, current_timestamp, unix_timestamp


class TaxiDataProcessor:

    def __init__(self, parquet_path: str):
        self.parquet_path = parquet_path
        self.spark = SparkSession.builder.appName("Tratamento e Armazenamento de Dados de Táxi com PySpark").getOrCreate()
        self.df = None

    def carregar_dados(self):
        self.df = self.spark.read.parquet(self.parquet_path)
        print("Esquema dos dados:")
        self.df.printSchema()

    def tratar_dados(self):
        df = self.df

        # Conversão de timestamp
        df = df.withColumnRenamed("tpep_pickup_datetime", "pickup_datetime")
        df = df.withColumnRenamed("tpep_dropoff_datetime", "dropoff_datetime")

        # Duração da viagem
        df = df.withColumn("trip_duration",(unix_timestamp("dropoff_datetime") - unix_timestamp("pickup_datetime")) / 60)

        # Tratamento de nulos
        df = df.fillna({"passenger_count": 1,"fare_amount": 0,"tip_amount": 0,"total_amount": 0})

        # Conversão de tipos
        df = df.withColumn("trip_distance", col("trip_distance").cast("float"))
        df = df.withColumn("fare_amount", col("fare_amount").cast("float"))
        df = df.withColumn("tip_amount", col("tip_amount").cast("float"))
        df = df.withColumn("total_amount", col("total_amount").cast("float"))

        # Transformações extras
        df = df.withColumn("last_updated", current_timestamp())
        df = df.withColumn("pickup_date", to_date(col("pickup_datetime")))

        # Remover colunas desnecessárias
        df = df.drop("store_and_fwd_flag", "Airport_fee", "cbd_congestion_fee")

        # Selecionar apenas as colunas que você quer no banco
        df = df.select(
            "VendorID", "pickup_datetime", "dropoff_datetime", "passenger_count",
            "trip_distance", "RatecodeID", "PULocationID", "DOLocationID",
            "payment_type", "fare_amount", "extra", "mta_tax", "tip_amount",
            "tolls_amount", "improvement_surcharge", "total_amount",
            "congestion_surcharge", "trip_duration", "last_updated", "pickup_date"
        )

        self.df = df

    def salvar_dados_processados(self, output_path: str):
        self.df.coalesce(1).write.mode("overwrite").parquet(output_path)

    def encerrar(self):
        self.spark.stop()
