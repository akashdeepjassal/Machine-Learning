from math import sqrt
import numpy as np
from collections import Counter
import pandas as pd
import random


dataset={'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features=[5,7]



def k_nearest_neighbors(data,predict,k=3):
    if len(data) >= k:
        warning.warn('K is less than total voting groups')
        #knnalgos
    distances=[]
    for group in data:
        for features in data[group]:
            eucledian_distance=np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([eucledian_distance,group])
    votes=[i[1] for i in sorted(distances)[:k]]
    # print(Counter(votes).most_common(1))
    vote_results=Counter(votes).most_common(1)[0][0]


    return vote_results

df=pd.read_csv('breast-cancer-wisconsin_data.txt')
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)
# print(df.head())
full_data=df.astype(float).values.tolist() #to convert any string to float
# print(full_data[:10])

random.shuffle(full_data)   #Shuffle data
# print(full_data[:10])

test_size=0.2
train_set={2:[],4:[]}
test_set={2:[],4:[]}
train_data=full_data[:-int(test_size*len(full_data)) ]
test_data=full_data[-int(test_size*len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct=0
total=0

for group in test_set:
    for data in test_set[group]:
        vote=k_nearest_neighbors(train_set,data,k=5)
        if group == vote:
            correct+=1
        total+=1

print('Accuracy:', correct/total)
