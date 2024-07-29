import requests

def fetchAndSAveToFile(url,path):
    r= requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)


url = "https://timesofindia.indiatimes.com/city/ahmedabad"

fetchAndSAveToFile(url,"data/times.html")