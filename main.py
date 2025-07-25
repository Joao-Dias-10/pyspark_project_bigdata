import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

from src.utils.spark_session_factory import SparkSessionFactory     
from src.utils.logger import LoggerConfig
from src.utils.excluder import Excluder
from src.utils.parquet_helper import ParquetHelper
from src.utils.config import (
    HADOOP,
    PARTIAL_URL_TRIP_YELLOW_TAXI,
    PATH_DATA_RAW,
    PATH_DATA_PROCESSED,
    JDBC_URL,
    GET_JDBC_PROPERTIES,
    JDBC_DRIVER_PATH
)

from src.automation.downloads import Downloads
from src.preprocessing.taxi_data_processor import TaxiDataProcessor

from src.db.models import Base
from src.db.init_db import engine
from src.db.queries import Inserter


def run():
    try:

        log_config = LoggerConfig(
            log_path='./logs',
            log_filename='execucao.log',
            log_level='DEBUG',
            logger_name='app'
        )
        logger = log_config.configurar()

        logger.info("Logger configurado. Iniciando pipeline e SparkSessionFactory e configurando ambiente Hadoop.")
        spark_factory = SparkSessionFactory(app_name="PipelineSpark")
        spark = spark_factory.create()

        logger.info("SparkSessionFactory configurado. Limpando diretórios de dados.")
        Excluder(PATH_DATA_RAW).clear_contents()
        Excluder(PATH_DATA_PROCESSED).clear_contents()

        logger.info("Diretórios limpos. Gerando URL para download.")
        data_suffix = (datetime.now() - relativedelta(months=3)).strftime("%Y-%m")
        file = f"{data_suffix}.parquet"
        full_url = f"{PARTIAL_URL_TRIP_YELLOW_TAXI}{file}"

        logger.info(f"URL gerada. Iniciando download do arquivo: {file}")
        downloader = Downloads()
        parquet_path = downloader.download_file(full_url, file)

        logger.info("Download finalizado. Iniciando processamento com Spark.")
        processor = TaxiDataProcessor(parquet_path, spark)
        processor.carregar_dados()
        processor.tratar_dados()

        logger.info("Processamento finalizado. Salvando arquivo tratado.")
        output_path = os.path.join(PATH_DATA_PROCESSED, file)
        processor.salvar_dados_processados(output_path)

        logger.info("Arquivo salvo. Gerando caminho do arquivo '.parquet' gerado pelo spark.")
        parquet_gerado_path = ParquetHelper.localizar_arquivo_parquet(output_path)

        logger.info("Caminho gerado. Criando tabelas no banco, se necessário.")
        Base.metadata.create_all(engine)

        logger.info("Tabelas verificadas. Iniciando inserção dos dados no PostgreSQL.")
        inserter = Inserter(
            spark=spark,
            jdbc_url=JDBC_URL,
            properties=GET_JDBC_PROPERTIES(),
            jdbc_driver_path=JDBC_DRIVER_PATH
        )
        inserter.insert(parquet_path=parquet_gerado_path, table_name="yellow_tripdata")
        
        logger.info("Inserção finalizada. Pipeline concluído com sucesso.")

    except Exception as e:
        logger.error(f"Erro registrado: {e}", exc_info=True)

    finally:
        if spark:
            spark.stop()
            logger.info("SparkSession finalizada com sucesso.\n\n")

if __name__ == "__main__":
    run()
