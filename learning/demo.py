import pandas as pd
import os as sys
import _datetime as dt
data= pd.read_csv(".venv/lib/n50.csv")

print(data.head(5))

date1=dt.datetime.today()
datetme=date1+dt.timedelta(hours=16,minutes=45)
# dte=date1.tz_localize("IST")
print(datetme)



