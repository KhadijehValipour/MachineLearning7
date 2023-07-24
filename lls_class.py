import numpy as np
import pandas as pd

class lls :
    def __init__(self):
        self.slope = None

    #trainning
    def fit(self,X,Y):
        self.X_train = X
        self.Y_train = Y
        self.slope = np.matmul(np.matmul(np.linalg.inv( np.matmul(self.X_train.T , self.X_train )) , self.X_train.T) , self.Y_train)
        return self.slope
    
    def predict(self,X_test) :
        Y=[]
        for x in X_test :
            y_pred = np.matmul(X_test, self.slope)
            Y.append(y_pred)
            
        return Y