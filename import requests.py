import requests

url = "https://in.finance.yahoo.com/quote/GATI.NS?p=GATI.NS"

response = requests.get(url)
Indicators = ["Previous Close",
            "Open",
            "Bid"
            "Ask"
            "Day's range",
            "52 Week Range"]
print(response)
print(response.status_code)

htmlText = response.text
splitList = htmlText.split("Previous Close")
print("Search to find")
firstsplit = splitList.split("\">")[1]
print(firstsplit)