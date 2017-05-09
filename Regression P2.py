import pandas as pd
import quandl
quandl.ApiConfig.api_key = '4p918nYkAPj-_7fYFEaf'
df=quandl.get("WIKI/AMZN")            #data frame

print df.head()

df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100.00
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.00
df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(df.head())
