import matplotlib.pyplot as pyplot
from matplotlib import style
style.use('ggplot')
import numpy as np

class Support_Vector_Machine:
    def __init__(self,visualization=True):
        self.visualization = visualization
        self.colors={1:'r',-1:'b'}
        if self.visualization:
            self.fig=plt.figure()
            self.ax=self.fig.add_subplot(1,1,1)

    def fit(self, data):
        # train
        self.data=data
        opt_dict=[]
        # { mod(w): [w,b] }
        transforms =[[1,1],
                     [-1,1],
                     [-1,-1],
                     [1,-1]]

         # apply to vector w
         all_data = []
         for yi in self.data:
             for featureset in self.data[yi]:
                 for feature in featureset:
                     all_data.append(feature)

        self.max_feature_value=max(all_data)
        self.max_feature_value=min(all_data)
        all_data = None

        step_sizes=[self.max_feature_value * 0.1,
                   self.max_feature_value * 0.01,
                   # point of expense
                   self.max_feature_value * 0.001,]
        # extremely expensive
        b_range_multiple = 5
        #
        b_multiple = 5

        # first elemet in value w
        lates_optimum=self.max_feature_value * 10

        for step in step_sizes:
            w=np.array([lates_optimum,lates_optimum])
            # DUE TO CONVEX PROBLEM
            optimized = False
            while not optimized:
                pass








    def predict(self,features):
        # sign(x.w+b)
        classification = np.sign(np.dot(np.array(features),self.w)+self.b)

        return classification




data_dict={-1:np.array([[1,7],
                       [2,8],
                       [3,8],]),
           1:np.array([[5,1],
                       [6,-1],
                       [7,3]])}
