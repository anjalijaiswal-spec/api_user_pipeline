import requests
import pandas as pd
import json

def dataimport(url,symbol,apikey):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&z7zdatatype=csv&apikey=UQI9C6RZV238CLP3"
    r = requests.get(url)
    data=r.json()

    ts=data.get("Time Series (Daily)")
# print(ts)

dates=sorted(ts.keys(),reverse=True)
# print(dates)

y_close=float(ts[dates[1]]["4. close"])
print(y_close)

t_close=float(ts[dates[0]]["4. close"])

print=t_close
m_senti=y_close-t_close
print(m_senti)


