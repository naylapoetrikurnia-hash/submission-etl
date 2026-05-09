import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine


def load_data(df):

    try:

        # ======================
        # SAVE CSV
        # ======================

        df.to_csv("products.csv", index=False)

        print("Data berhasil disimpan ke CSV")

        # ======================
        # SAVE GOOGLE SHEETS
        # ======================

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "google-sheets-api.json",
            scope
        )

        client = gspread.authorize(creds)

        spreadsheet = client.open_by_key(
            "1avogYpGysORP1giZRqJVt4ujRkPFPwzEOAttRjSdBG4"
        )

        worksheet = spreadsheet.sheet1

        worksheet.clear()

        # CONVERT TIMESTAMP TO STRING
        df["timestamp"] = df["timestamp"].astype(str)

        worksheet.update(
            [df.columns.values.tolist()] + df.values.tolist()
        )

        print("Data berhasil disimpan ke Google Sheets")

        # ======================
        # SAVE POSTGRESQL
        # ======================

        engine = create_engine(
             "YOUR_POSTGRESQL_CONNECTION"
        )

        df.to_sql(
            "fashion_products",
            engine,
            if_exists="replace",
            index=False
        )

        print("Data berhasil disimpan ke PostgreSQL")

    except Exception as e:

        print(f"Error saat menyimpan data: {e}")