import pandas as pd

def transform_data(data):

    df = pd.DataFrame(data)

    # ======================
    # TRANSFORM PRICE
    # ======================

    df["Price"] = df["Price"].str.replace("$", "", regex=False)

    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    df["Price"] = df["Price"] * 16000

    # ======================
    # TRANSFORM RATING
    # ======================

    df["Rating"] = df["Rating"].str.extract(r'(\d+\.\d+)')

    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

    # ======================
    # TRANSFORM COLORS
    # ======================

    df["Colors"] = df["Colors"].str.extract(r'(\d+)')

    df["Colors"] = pd.to_numeric(df["Colors"], errors="coerce")

    # ======================
    # CLEAN SIZE
    # ======================

    df["Size"] = df["Size"].str.replace("Size: ", "", regex=False)

    # ======================
    # CLEAN GENDER
    # ======================

    df["Gender"] = df["Gender"].str.replace("Gender: ", "", regex=False)

    # ======================
    # CLEANING DATA
    # ======================

    df = df[df["Title"] != "Unknown Product"]

    df = df.dropna()

    df = df.drop_duplicates()

    df = df.reset_index(drop=True)

    return df