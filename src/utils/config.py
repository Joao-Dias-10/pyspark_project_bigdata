import os
from dotenv import load_dotenv

# Caminho relativo para o .env
ENV_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'config', '.env')
load_dotenv(ENV_PATH)

# Variáveis de caminhos e URLs externas
PARTIAL_URL_TRIP_YELLOW_TAXI = os.getenv("PARTIAL_URL_TRIP_YELLOW_TAXI")
PATH_DATA_RAW = os.getenv("PATH_DATA_RAW")
PATH_DATA_PROCESSED = os.getenv("PATH_DATA_PROCESSED")
HADOOP = os.getenv("HADOOP")

# Conexão com banco via JDBC (PySpark)
JDBC_URL = os.getenv("JDBC_URL")

#URL do SQLAlchemy 
SQLALCHEMY_URL =os.getenv("SQLALCHEMY_URL")

# Variáveis de banco para SQLAlchemy (ORM)
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")

JDBC_DRIVER_PATH = os.getenv("JDBC_DRIVER_PATH")

def GET_JDBC_PROPERTIES() -> dict:
    return {
        "user": os.getenv("PG_USER"),
        "password": os.getenv("PG_PASSWORD"),
        "driver": "org.postgresql.Driver"
    }

def COLUMN_RENAME_MAP() -> dict: 
    
    return {
        "VendorID": "vendor_id",
        "RatecodeID": "ratecode_id",
        "PULocationID": "pu_location_id",
        "DOLocationID": "do_location_id",
        "tpep_pickup_datetime": "pickup_datetime",
        "tpep_dropoff_datetime": "dropoff_datetime"
    }

