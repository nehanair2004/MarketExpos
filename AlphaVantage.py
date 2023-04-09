import requests

url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=KQWP5RDPL7XFZVEK'
r = requests.get(url)
data = r.json()


print(data["DividendPerShare"])
print(data["52WeekLow"])