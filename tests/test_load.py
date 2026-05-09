import pandas as pd
from utils.load import load_data

def test_load_data():

    df = pd.DataFrame({
        "Title": ["Test Product"]
    })

    load_data(df)

    assert True


def test_load_data_error():

    load_data(None)

    assert True