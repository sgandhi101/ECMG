import yfinance as yf
import pandas as pd
import json
import quandl
from yfHistoricals import getHistory

quandl.ApiConfig.api_key = 'VP3AoTe9zax2xk-o_Eq-'
auth_tok = "VP3AoTe9zax2xk-o_Eq-"

def getHistorical(ticker, startDate, endDate):
    data = quandl.get("WIKI/" + ticker.upper(), trim_start = str(startDate), trim_end = str(endDate), authtoken=auth_tok)
    data.to_csv(r"historical" + ticker.upper() +".csv", index=True, header=True)
    print("Historical data successfully written to CSV!")


while True:
    tickerName = input("Which ticker's information do you want? ")
    ticker = yf.Ticker(tickerName)
    try:
        information = ticker.info
        break
    except:
        pass

#########ADDITIONAL POTENTIAL TBD THIS LATER##########
hist = ticker.history(period="5d")
#print(hist)

with open(tickerName.upper() + "info.json", "w") as outfile:  
    json.dump(information, outfile)
print("Information written to file!")

while True:
    historicalBool = input("Do you want historical data? Enter yes or no: ")
    historicalBool = historicalBool.lower()
    if(historicalBool=="yes" or historicalBool=="no"):
        if historicalBool=="yes":
            startDate = input("What start date? Enter as YEAR-MONTH-DAY: ")
            endDate = input("What end date? Enter as YEAR-MONTH-DAY: ")
            getHistory(tickerName, startDate, endDate)
            break
        else:
            break
    else:
        pass