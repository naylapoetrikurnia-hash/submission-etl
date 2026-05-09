from utils.extract import scrape_data
import requests
from unittest.mock import patch

def test_scrape_data():

    data = scrape_data()

    assert data is not None
    assert len(data) > 0


@patch("utils.extract.requests.get")
def test_scrape_data_error(mock_get):

    mock_get.side_effect = requests.exceptions.RequestException

    data = scrape_data()

    assert data == []