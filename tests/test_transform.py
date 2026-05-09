from utils.transform import transform_data

def test_transform_data():

    sample_data = [
        {
            "Title": "Test Product",
            "Price": "$100",
            "Rating": "Rating: 4.5 / 5",
            "Colors": "3 Colors",
            "Size": "Size: M",
            "Gender": "Gender: Men",
            "timestamp": "2025-01-01"
        }
    ]

    df = transform_data(sample_data)

    assert not df.empty


def test_transform_data_error():

    df = transform_data(None)

    assert df.empty