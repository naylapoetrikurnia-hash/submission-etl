from utils.transform import transform_data

def test_transform_data():

    sample_data = [
        {
            "Title": "T-shirt",
            "Price": "$100",
            "Rating": "Rating: ⭐ 4.5 / 5",
            "Colors": "3 Colors",
            "Size": "Size: M",
            "Gender": "Gender: Men"
        }
    ]

    df = transform_data(sample_data)

    assert df is not None
    assert not df.empty