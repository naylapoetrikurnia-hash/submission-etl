def load_data(df):

    try:

        df.to_csv("products.csv", index=False)

        print("Data berhasil disimpan ke products.csv")

    except Exception as e:

        print(f"Error saat menyimpan data: {e}")