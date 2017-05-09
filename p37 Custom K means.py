import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np



X=np.array([[1,2],
           [1.5,1.8],
           [5,8],
           [8,8],
           [1,0.6],
           [9,11]])

plt.scatter(X[:,0],X[:,1],s=40)
plt.show()

colors=10*['g.','r.','c.','b.','k.']

class K_Means:
    def __init__(self,k=2,tol=0.001, max_iter=300):
        self.k =k
        self.tol=tol
        self.max_iter=max_iter

    def fit(self,data):
        self.centroids={}
        dor i in range(self.k):
            self.centroids[i]=data[i]

        for in range(self.max_iter):
            self.clssifications={}

            for i in range(self.k):
                self.clssificatins[i]=[]

            for featureset in X:
                distances=[np.linalg.norm(gfeatureset-self.centroids[centroid])for centroid in self.centroid]
                classification=distances.index(min(distances))
                self.classification[classification].append(featureset)

        prev_centroids=dict(self.centroids)
        for classification in self.classifications:
            pass
            self.centroids[classification=np.average(self.classificatins[classification],axis=0)
            
        
                    

    def predict(self,data):
        pass

    
