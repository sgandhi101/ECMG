import yfinance as yf
import json

def getHistory(ticker, startDate, endDate):
    data = yf.download(str(ticker), start=str(startDate), end=str(endDate), group_by = 'column')
    data.to_csv(r"historicals" + str(ticker.upper()) + ".csv", index=True, header=True)
    print("Historical data operation successful!")

"""
Useful Link:
https://github.com/GregBland/yfinance_article/blob/master/example_code.ipynb
"""