import os
import logging
from src.utils.logger import LoggerConfig

def test_logger_configuracao_tem_handlers(tmp_path):
    log_dir = tmp_path / "logs"
    logger_config = LoggerConfig(log_path=str(log_dir), log_filename="teste.log", log_level="DEBUG", logger_name="test_logger")
    logger = logger_config.configurar()

    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.DEBUG
    assert logger.hasHandlers()
