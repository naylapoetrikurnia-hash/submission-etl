from extract import scrape_data
from transform import transform_data
from load import save_to_csv

# EXTRACT
data = scrape_data()

print("Total data hasil scraping:", len(data))

# TRANSFORM
df = transform_data(data)

print("Shape data setelah cleaning:", df.shape)

print(df.head())

print(df.info())

# LOAD
save_to_csv(df)