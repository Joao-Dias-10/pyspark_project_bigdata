import os
from pyspark.sql import SparkSession
from src.utils.config import JDBC_DRIVER_PATH, HADOOP


class SparkSessionFactory:
    def __init__(self, app_name: str = "pyspark_project_bigdata"):
        self.app_name = app_name
        self._configure_environment()
        self.spark = None

    def _configure_environment(self):
        # Configura variáveis de ambiente do Hadoop
        os.environ["HADOOP_HOME"] = HADOOP
        os.environ["PATH"] += os.pathsep + os.path.join(HADOOP, "bin")

    def create(self) -> SparkSession:
        if not self.spark:
            self.spark = SparkSession.builder \
                .appName(self.app_name) \
                .config("spark.jars", JDBC_DRIVER_PATH) \
                .getOrCreate()
        return self.spark
