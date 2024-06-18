'''
CSV data will need to be sanitized.  Namely the founded year.  It is a str field and has no standardization
'''

import json
import pandas
import pathlib
import yfinance
import datetime

today = datetime.date.today()
config_path = pathlib.Path.cwd() / "shared" / "config.json"
config_file = json.load(open(config_path))
load_file = pathlib.Path(config_file["stock_analysis"]["load_file"])

csv_data = pandas.read_csv(load_file)
#plot current stock price to years of existence (current year - founded)
#test - get 7day average for closing cost
symbols = list(csv_data["Symbol"])

'''
because the yahoo api needs a list of symbols as a parameter to pull initial data, we have to 
reassign the symbols list to what is successfully pulled (some symbols in the spreadsheet might fail
to return anything from yahoo
'''
#grab data from yahoo for each symbol in spreadsheet
tickers = yfinance.download(" ".join(symbols), start=(today - datetime.timedelta(days=12)), end=today)
symbols = list(tickers["Adj Close"].columns)

closing_avg = []
age = []
for i in range(len(symbols)):
    closing_avg.append(tickers["Adj Close"][symbols[i]].mean())
    age.append(today.year - int(csv_data[csv_data.Symbol == symbols[i]].Founded))
    

