import requests
from bs4 import BeautifulSoup
import pandas as pd


data = {'title':[] , 'price':[]}
url = "https://www.amazon.in/s?k=iphone&crid=1UNJ6FKP70S1E&sprefix=iphone%2Caps%2C213&ref=nb_sb_noss_1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



r= requests.get(url,headers = headers)

soup = BeautifulSoup(r.content,'html.parser')
#print(soup.prettify())

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
for span in spans:
    title = span.get_text()
    print(title)
    data["title"].append(title)

for price in prices:
    if "a-text-price" not in price.get('class'):
        price_text = price.find("span").get_text()
        price_text = price_text.replace('₹', '').replace(',', '').replace(' ', '').replace('\xa0', '')
        print(price_text)
        data['price'].append(price_text)
        if len(data["price"]) == len(data["title"]):
            break


df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv",index=False)






