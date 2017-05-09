import pandas as pd
import quandl
import math,datetime,time
import numpy as np
from sklearn import preprocessing, cross_validation,svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

quandl.ApiConfig.api_key = '4p918nYkAPj-_7fYFEaf'
df=quandl.get("WIKI/AMZN")            #data frame

#print df.head()
#features
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100.00
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.00
df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

#print(df.head())

forecast_col='Adj. Close'
df.fillna(-99999, inplace=True) #Pandas give Nan data so this value is added

forecast_out=int(math.ceil(0.01*len(df)))  #1% of Data Frame , Data from 10 days ago
print(forecast_out)
# print(forecast_out)

#labels
df['label']=df[forecast_col].shift(-forecast_out) #Shifting column negatively
# print(df.head())

# X for features , y for labels

X = np.array(df.drop(['label','Adj. Close'],1))
X=preprocessing.scale(X)
X_lately=X[-forecast_out:]
X=X[:-forecast_out:]


df.dropna(inplace=True)

y=np.array(df['label'])
y = np.array(df['label'])

# print len(X),len(y)

# Create Training Examples
X_train, X_test, y_train, y_test=cross_validation.train_test_split(X,y,test_size=0.2)
#define classifier
clf=LinearRegression()
# clf=LinearRegression(n_jobs=no_of_threads_you_want)
clf.fit(X_train,y_train)
#accuracy
accuracy=clf.score(X_test,y_test)

# print('accuracy with LinearRegression is %f'%accuracy)

forecast_set=clf.predict(X_lately)    #enter a single value or array

print(forecast_set,accuracy,forecast_out)

df['Forecast']=np.nan

last_date=df.iloc[-1].name
last_unix=time.mktime(last_date.timetuple())
one_day=86400
next_unix= last_unix + one_day


for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date]=[np.nan for _ in range(len(df.columns)-1)]+[i]


df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
