import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2018, 2, 8)

df = web.DataReader('TSLA', start, end)

print(df.head())
