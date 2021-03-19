import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('Dataset1.xlsx')

def cost(P,T):
    return(P-T)**2

def slope_cost(P,T):
    h=0.001
    return (cost(P+h,T)-cost(P,T))/h

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))

w1=np.random.randn()
w2=np.random.randn()
b1=np.random.randn()

w3=np.random.randn()
w4=np.random.randn()
b2=np.random.randn()


learning_rate=0.2
costs=[]

for i in range(999999):
    print(i)
    rn=np.random.randint(len(df['delx']))
    point=df['Jump'][rn]

    x1=df['delx'][rn]
    x2=df['dely'][rn]

    z1=x1*w1+x2*w2+b1
    pred1=sigmoid(z1)
    target1=df['Jump'][rn]
    slope_cost_1=slope_cost(pred1,target1)
    derivative_pred1=sigmoid_p(z1)
    modified_weights_bias1=slope_cost_1*derivative_pred1

    z2=x1*w3+x2*w4+b2
    pred2=sigmoid(z2)
    target2=df['Duck'][rn]
    slope_cost_2=slope_cost(pred2,target2)
    derivative_pred2=sigmoid_p(z2)
    modified_weights_bias2=slope_cost_2*derivative_pred2


    w1=w1-learning_rate*modified_weights_bias1*x1
    w2=w2-learning_rate*modified_weights_bias1*x2
    b1=b1-learning_rate*modified_weights_bias1

    w3=w3-learning_rate*modified_weights_bias2*x1
    w4=w4-learning_rate*modified_weights_bias2*x2
    b2=b2-learning_rate*modified_weights_bias2






with open('weights_so_far1.txt','w+')as f:
    f.writelines(str(w1))
    f.writelines('\n')
    f.writelines(str(w2))
    f.writelines('\n')
    f.writelines(str(b1))
    f.writelines('\n')
    f.writelines(str(w3))
    f.writelines('\n')
    f.writelines(str(w4))
    f.writelines('\n')
    f.writelines(str(b2))
    f.writelines('\n')
