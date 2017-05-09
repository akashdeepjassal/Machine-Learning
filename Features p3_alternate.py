import pandas as pd
import quandl
import math
quandl.ApiConfig.api_key = '4p918nYkAPj-_7fYFEaf'
df=quandl.get("WIKI/AMZN")            #data frame

#print df.head()

#features
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100.00
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.00
df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(df.head())

forecast_col='Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out=int(math.ceil(0.1*len(df)))


#labels
df['label']=df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.tail())
