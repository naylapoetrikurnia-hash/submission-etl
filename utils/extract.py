import requests
from bs4 import BeautifulSoup

def scrape_data():

    base_url = "https://fashion-studio.dicoding.dev"

    data = []

    for page in range(1, 51):

        if page == 1:
            url = base_url
        else:
            url = f"{base_url}/page{page}"

        print(f"Scraping page {page}: {url}")

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("div", class_="collection-card")

        for product in products:

            title = product.find("h3", class_="product-title").text

            price_tag = product.find("span", class_="price")

            if price_tag:
                price = price_tag.text
            else:
                price = "Price Unavailable"

            details = product.find_all("p")

            rating = "No Rating"
            colors = "No Colors"
            size = "No Size"
            gender = "No Gender"

            for detail in details:

                text = detail.text

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
                "Gender": gender
            }

            data.append(product_data)

    return data