from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

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
    print(Counter(votes).most_common(1))
    vote_results=Counter(votes).most_common(1)[0][0]


    return vote_results

result=k_nearest_neighbors(dataset,new_features,k=3)
print(result)

[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0],new_features[1])
plt.show()
