import json
import pandas
import pathlib
import yfinance
import datetime

today = datetime.date.today()
config_path = pathlib.Path.cwd() / "shared" / "config.json"
config_file = json.load(open(config_path))
load_file = pathlib.Path(config_file["stock_analysis"]["load_file"])

data = pandas.read_csv(load_file)
#plot current stock price to years of existence (current year - founded)
#test - get 7day average for closing cost
symbols = list(data["Symbol"])
closing_avg = [0 * len(symbols)]
age = list(data["Founded"])


#grab data from yahoo for each symbol in spreadsheet
tickers = yfinance.download(" ".join(symbols), start=(today - datetime.timedelta(days=12)), end=today)

for i in range(len(symbols)):
    closing_avg[i] = tickers["Adj Close"][symbols[i]].mean()
    age[i] = today.year - int(age[i])
    
print(closing_avg[:10])
print(age[:10])