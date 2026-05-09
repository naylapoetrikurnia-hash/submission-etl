import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_data():

    base_url = "https://fashion-studio.dicoding.dev"

    data = []

    try:

        for page in range(1, 51):

            if page == 1:
                url = base_url
            else:
                url = f"{base_url}/page{page}"

            print(f"Scraping page {page}: {url}")

            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            products = soup.find_all("div", class_="collection-card")

            for product in products:

                title = product.find("h3", class_="product-title").text.strip()

                price_tag = product.find("span", class_="price")

                if price_tag:
                    price = price_tag.text.strip()
                else:
                    price = "Price Unavailable"

                details = product.find_all("p")

                rating = "No Rating"
                colors = "No Colors"
                size = "No Size"
                gender = "No Gender"

                for detail in details:

                    text = detail.text.strip()

                    if "Rating" in text or "Not Rated" in text:
                        rating = text

                    elif "Colors" in text:
                        colors = text

                    elif "Size" in text:
                        size = text

                    elif "Gender" in text:
                        gender = text

                product_data = {
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Colors": colors,
                    "Size": size,
                    "Gender": gender,
                    "timestamp": datetime.now()
                }

                data.append(product_data)

    except Exception as e:
        print(f"Error saat scraping data: {e}")

    return data