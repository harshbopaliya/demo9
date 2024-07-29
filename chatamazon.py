import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

data = {'title': [], 'price': []}
url = "https://www.amazon.in/s?k=iphone&crid=1UNJ6FKP70S1E&sprefix=iphone%2Caps%2C213&ref=nb_sb_noss_1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    
    soup = BeautifulSoup(r.content, 'html.parser')

    spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
    prices = soup.select("span.a-price")

    for span in spans:
        title = span.get_text(strip=True)
        print(title)
        data["title"].append(title)

    for price in prices:
        if price.find_parent("a") and "a-text-price" not in price.get('class'):
            price_text = price.find("span", class_="a-offscreen").get_text(strip=True)
            # Clean up price text to remove non-numeric characters
            price_text = re.sub(r'[^\d.]', '', price_text)
            print(price_text)
            data['price'].append(price_text)
            if len(data["price"]) == len(data["title"]):
                break

    # Ensure the lengths of title and price lists are the same
    max_length = max(len(data["title"]), len(data["price"]))
    data["title"].extend([None] * (max_length - len(data["title"])))
    data["price"].extend([None] * (max_length - len(data["price"])))

    df = pd.DataFrame.from_dict(data)

    df.to_csv("cdata.csv", index=False)
    df.to_excel("cdata2.xlsx", index=False)

    print("Data has been written to cdata.csv and cdata2.xlsx")

except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
