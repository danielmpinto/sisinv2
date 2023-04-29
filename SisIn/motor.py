import pandas as pd
from pytrends.request import TrendReq
import time



def Gstrends():
    pytrends=TrendReq(hl='en-US', tz=360)
    kw_list=['febre','tosse','garganta','hospital']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR',gprop='')
    testef=pytrends.interest_over_time()

    del testef['isPartial']
    return testef
 
def Ligar(): 
          results=Gstrends()
          results.to_excel('google.xlsx')
"""
def Ligar():
    for i in range(1000):     
          results=Gstrends()
          results.to_excel('google.xlsx')
          time.sleep(30)"""