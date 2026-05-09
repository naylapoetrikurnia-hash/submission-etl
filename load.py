def save_to_csv(df):

    df.to_csv("products.csv", index=False)

    print("Data berhasil disimpan ke products.csv")