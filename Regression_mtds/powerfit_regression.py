import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([12,300,550,900,1400])

x2y_sum = 0
for i in range (len(x)):
    x2y_sum+= x[i] * x[i] * y[i]

x4_sum = 0
for i in range(len(x)):
    x4_sum += (x[i])**4

a = x2y_sum/x4_sum
print(a)