import os
import pytest
from unittest.mock import patch, mock_open
from src.automation.downloads import Downloads

@patch("src.automation.downloads.requests.get")
def test_download_file_success(mock_get, tmp_path):
    # Arrange
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.content = b"dummy parquet content"

    download = Downloads(path_raw=str(tmp_path))
    test_url = "http://example.com/file.parquet"
    test_file = "test.parquet"
    
    # Act
    path = download.download_file(test_url, test_file)

    # Assert
    assert os.path.exists(path)
    with open(path, "rb") as f:
        content = f.read()
    assert content == b"dummy parquet content"
