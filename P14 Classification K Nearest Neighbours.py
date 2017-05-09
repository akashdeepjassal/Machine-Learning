import numpy as np
from sklearn import preprocessing,cross_validation,neighbors
import pandas as pd

df=pd.read_csv('breast-cancer-wisconsin_data.txt')
df.replace('?',-99999,inplace=True)   #-99999 is outlier pandas and other libraries see it as outlier so as to not drop data
df.drop(['id'],1,inplace=True)

X=np.array(df.drop(['class'],1))
y=np.array(df['class'])

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)


clf=neighbors.KNeighborsClassifier(n_jobs=-1)
clf.fit(X_train,y_train)

accuracy=clf.score(X_test,y_test)
print(accuracy)

example_measures=np.array([[4,2,1,1,1,2,3,2,1],[10,8,8,6,6,5,7,7,4],[0,0,0,0,0,0,0,0,0]])
example_measures=example_measures.reshape(len(example_measures),-1)

prediction=clf.predict(example_measures)
print(prediction)
