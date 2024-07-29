import csv
from bs4 import BeautifulSoup
import requests

# Example URL (replace with the actual URL you want to scrape)
url = "https://www.amazon.in/s?k=iphone&crid=1UNJ6FKP70S1E&sprefix=iphone%2Caps%2C213&ref=nb_sb_noss_1"

# Send a request to fetch the page content
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Create a dictionary to store the data
data = {
    "title": [],
    "price": []
}

# Select the HTML elements containing product titles and prices
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")

# Extract and print/store the product titles
for span in spans:
    title = span.get_text()
    print(title)
    data["title"].append(title)

# Extract and print/store the product prices
for price in prices:
    if "a-text-price" not in price.get("class"):
        price_text = price.find("span").get_text()
        print(price_text)
        data["price"].append(price_text)

# Write the data to a CSV file
with open('ama.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(data['title'])):
        writer.writerow({'title': data['title'][i], 'price': data['price'][i]})

print("Data has been written to amazon_products.csv")
