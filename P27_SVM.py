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
        # { ||w||: [w,b] }
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
        # support vec = yi(xi.w+b)=1
        # 1.01
        step_sizes=[self.max_feature_value * 0.1,
                    self.max_feature_value * 0.01,
                    # point of expense
                    self.max_feature_value * 0.001,
                    self.max_feature_value * 0.0001,]



         # extremely expensive
        b_range_multiple = 5
         # no need to take small steps with w
        b_multiple = 5

         # first elemet in value w
        latest_optimum=self.max_feature_value * 10

        for step in step_sizes:
            w=np.array([latest_optimum,latest_optimum])
             # DUE TO CONVEX PROBLEM
            optimized = False
            while not optimized:

                for b in np.arange(-1*(self.max_feature_value*b_range_multiple),
                                    self.max_feature_value*b_range_multiple,
                                    step*b_multiple):
                    for transformation in transforms:
                        w_t=w*transformation
                        found_option=True
                        # Weakest link in SVM fundamentally
                        # SMO attempts to fix it
                        # yi(xi.w+b)>=1
                        for i in self.data:
                            for xi in self.data[i]:
                                yi=i
                                if not yi*(np.dot(w_t,xi)+b)>=1:
                                    found_option = False
                                    # BREAK TO SAVE TIME

                    if found_option:
                        opt_dict[np.linalg.norm(w_t)]=[w_t,b]         # magitude

                if w[0] < 0:
                    optimized = True
                    print('Optimized a step')
                else :
                    # w = [5,5]
                    # step =1
                    # w - [step,step] = [4,4]
                    w= w - step

            norms=sorted([n for n in opt_dict])
            opt_choice=opt_dict[norms[0]]
            # ||w||:[w,b]
            self.w=opt_choice[0]
            self.b=opt_choice[1]
            latest_optimum=opt_choice[0][0]+step*2



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
