from utils.extract import scrape_data

def test_scrape_data():

    data = scrape_data()

    assert data is not None
    assert len(data) > 0