import yfinance as yf
import pandas as pd
import yahoofinancials
import matplotlib
import lxml
import bs4
import requests
from bs4 import BeautifulSoup

class Stock_Data:
    def __init__(self):

      # tickerSymbol = 'MSFT'

      # msft = yf.Ticker("MSFT")

      ## get stock info
      # print(msft.info)

      # tickerData = yf.Ticker(tickerSymbol)

      # print(tickerData.info)

      # tickerDF = tickerData.history(period='1d', start='2010-1-1', end='2020-4-24')

      #  print(tickerDF[1])
        tsla_df = yf.download('DANSKE.CO',interval='1')

        print(tsla_df.head())

      # tsla_df = yf.download('TSLA')
      # print(tsla_df)

      #  ticker = yf.Ticker('TSLA')
#
      #  tsla_df = ticker.history(period="max")
#
      #  tsla_df['Close'].plot(title="TSLA's stock price")





    def GetStockPrice(self):
        pass
