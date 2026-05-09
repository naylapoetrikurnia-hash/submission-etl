from utils.extract import scrape_data
from utils.transform import transform_data
from utils.load import load_data

def main():

    # EXTRACT
    data = scrape_data()

    print("Total data hasil scraping:", len(data))

    # TRANSFORM
    df = transform_data(data)

    print("Shape data setelah cleaning:", df.shape)

    print(df.head())

    print(df.info())

    # LOAD
    load_data(df)

if __name__ == "__main__":
    main()