import matplotlib.pyplot as plt 
import numpy as np
import math
def funkcja(x):
    return(x*math.exp(-6*x))
def calka(f, xmin, xmax, n):
    h = (xmax - xmin) /n
    pole=0
    x =np.zeros(n)
    y =np.zeros(n)
    for i in range(n):
            x[i] = xmin + i*h
            y[i] = f(x[i])
            pole += (f(y[i]+i*h)+ f(xmin+(i+1)*h))*h/2
    print(pole)
    return x,y

x , y =calka(funkcja, 0.0, 1.5,1000)

plt.plot(x,y,'r-')