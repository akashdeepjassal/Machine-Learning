import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation,svm
from sklearn.linear_model import LinearRegression

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

forecast_out=int(math.ceil(0.01*len(df)))  #10% of Data Frame , Data from 10 days ago
print(forecast_out)

#labels
df['label']=df[forecast_col].shift(-forecast_out) #Shifting column negatively
df.dropna(inplace=True)
print(df.head())

# X for features , y for labels

X = np.array(df.drop(['label'],1))
y = np.array(df['label'])

X=preprocessing.scale(X)
# X=X[:-forecast_out+1]
# df.dropna(inplace=True)
y=np.array(df['label'])

# print len(X),len(y)

# Create Training Examples
X_train, X_test, y_train, y_test=cross_validation.train_test_split(X,y,test_size=0.2)
#define classifier
clf=svm.SVR()
clf.fit(X_train,y_train)
accuracy1=clf.score(X_test,y_test)
print('SVM accuracy without kernel is %f' %accuracy1)
clf=svm.SVR(kernel='poly')
clf.fit(X_train,y_train)
#accuracy
accuracy=clf.score(X_test,y_test)

print('SVM accuracy with kernel is %f' %accuracy)
