import quandl
import pandas
quandl.ApiConfig.api_key = 'VP3AoTe9zax2xk-o_Eq-'
auth_tok = "VP3AoTe9zax2xk-o_Eq-"

def getHistorical(ticker, startDate, endDate):
    data = quandl.get("WIKI/" + ticker, trim_start = str(startDate), trim_end = str(endDate), authtoken=auth_tok)
    data.to_csv(r"historical" + ticker +".csv", index=True, header=True)
    print("Historical data successfully written to CSV!")

tickerName = "aapl"
startDate = input("What start date? Enter as YEAR-MONTH-DAY: ")
endDate = input("What end date? Enter as YEAR-MONTH-DAY: ")

getHistorical(tickerName.upper(), startDate, endDate)
 