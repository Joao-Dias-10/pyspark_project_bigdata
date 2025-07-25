import os
import requests
from src.utils.config import PATH_DATA_RAW

class Downloads:

    def __init__(self, path_raw: str = PATH_DATA_RAW):
        self.path_raw = path_raw

    def download_file(self, full_url_with_date_suffix: str , file: str) -> str:

        file_path = os.path.join(self.path_raw, file)

        response = requests.get(full_url_with_date_suffix)
        response.raise_for_status()  # levanta erro se falhar
        with open(file_path, "wb") as f:
                f.write(response.content)

        return file_path
