import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', 'config', '.env'))

PARTIAL_URL_TRIP_YELLOW_TAXI = os.getenv("PARTIAL_URL_TRIP_YELLOW_TAXI")
PATH_DATA_RAW = os.getenv("PATH_DATA_RAW")
PATH_DATA_PROCESSED = os.getenv("PATH_DATA_PROCESSED")
HADOOP = os.getenv("HADOOP")
