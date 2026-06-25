import pandas as pd


def load_data(df: pd.DataFrame, output_file: str = "products.csv") -> None:
    """
    Menyimpan DataFrame ke dalam file CSV.

    Parameters:
        df: DataFrame yang akan disimpan.
        output_file: Nama atau lokasi file CSV.
    """
    try:
        df.to_csv(output_file, index=False)
        print(f"Data berhasil disimpan ke {output_file}")

    except Exception as error:
        print(f"Error saat menyimpan data ke CSV: {error}")
        raise