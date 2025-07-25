from src.utils.logger import LoggerConfig   
from src.utils.excluder import Excluder  
from src.utils.config import HADOOP, PARTIAL_URL_TRIP_YELLOW_TAXI, PATH_DATA_RAW, PATH_DATA_PROCESSED
from src.automation.downloads import Downloads
from src.preprocessing.taxi_data_processor import TaxiDataProcessor

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import os

def run():
    try:
  
        log_config = LoggerConfig(log_path='./logs',log_filename='execucao.log',log_level='DEBUG',logger_name='app' )
        logger = log_config.configurar()

        logger.info("Processo iniciado. Referenciando o hadoop para o pyspark usar.")
        os.environ["HADOOP_HOME"] = HADOOP
        os.environ["PATH"] += os.pathsep + rf"{HADOOP}\bin"

        logger.info("Hadoop configurado. limpando pasta data.")
        Excluder(PATH_DATA_RAW).clear_contents()
        Excluder(PATH_DATA_PROCESSED).clear_contents()

        logger.info("Pasta data limpa. Gerando url com sufixo de data de busca do arquivo.")
        full_url_with_date_suffix = f'{PARTIAL_URL_TRIP_YELLOW_TAXI}{(datetime.now() - relativedelta(months=3)).strftime("%Y-%m")}.parquet'
        
        logger.info("Url gerada. Gerando nome do arquivo com base na url.")
        file = full_url_with_date_suffix.rstrip("/").split("/")[-1]

        logger.info(rf"Nome do aquivo = {file} e Url de busca gerada = {full_url_with_date_suffix} Iniciando Download file.")
        downloader = Downloads()
        parquet_path = downloader.download_file(full_url_with_date_suffix, file)

        logger.info(f"Arquivo baixado: {parquet_path}. Iniciando processamento com Spark.")

        processor = TaxiDataProcessor(parquet_path)
        processor.carregar_dados()
        processor.tratar_dados()

        logger.info(f"Processamento finalizado. Salvando arquivo.parquet")
        output_path = os.path.join(PATH_DATA_PROCESSED, file)
        processor.salvar_dados_processados(output_path)

        processor.encerrar()
        logger.info("Processos finalizados com sucesso.\n\n")

    except Exception as e:
        logger.error(f"Erro registrado: {e}\n\n", exc_info=True)

if __name__ == "__main__":
    run()