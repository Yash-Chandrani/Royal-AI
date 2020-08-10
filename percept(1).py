# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 13:41:54 2020

@author: Yash Chandrani
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:18:01 2020

@author: Yash Chandrani
"""
import numpy as np

class percept(object):
    def __init__(self,no_of_inputs,threshold=100,learning_rate=.001):
        
        self.threshold=threshold
        self.learning_rate=learning_rate
        self.weights=np.zeros(no_of_inputs + 1)
        
    def predict(self,inputs):
        summ=np.dot(inputs,self.weights[1:])+self.weights[0]  #w.x + b
        if summ>0:
            activation=1
        else:
            activation=0
        return activation
    
    def train(self,training_inputs,labels):     #labels=correct output
        #x=1000
        count=0
        
        for _ in range(self.threshold): 
            for inputs,label in zip(training_inputs,labels): 
                prediction=self.predict(inputs)
                self.weights[1:]+=self.learning_rate*(label-prediction)*inputs
                self.weights[0]+=self.learning_rate*(label-prediction)
                y=(label-prediction)*prediction
                if(y>111):
                    count+=1
                else:
                    print(count)
            
            break;
        
        #print(_,end=" ")
        #print(prediction,end=" ")
        #print(self.weights)

training_inputs=[]
training_inputs.append(np.array([1,1]))
training_inputs.append(np.array([0,1]))
training_inputs.append(np.array([1,0]))
training_inputs.append(np.array([0,0]))
print(training_inputs)
labels=np.array([1,0,0,0])

percept=percept(2) #class name=obj name()
percept.train(training_inputs,labels)

inputs=np.array([0,0])
print(percept.predict(inputs))