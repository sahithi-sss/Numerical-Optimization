import numpy as np

x = np.array([1500,1600,1700,1800,2000])
y = np.array([245,265,275,295,325])

y_sum = 0
for i in range(len(y)):
    #print(i)
    y_sum += y[i]

x_sum = 0
for i in range(len(x)):
    #print(i)
    x_sum += x[i] 

x2_sum = 0
for i in range(len(x)):
    #print(i)
    x2_sum += x[i]* x[i]

xy_sum = 0
for i in range(len(x)):
    #print(i)
    xy_sum += x[i]* y[i]

y_mean = y_sum / 5
x_mean = x_sum / 5

n = 5
b = ((n* xy_sum) - (x_sum * y_sum)) / ((n* x2_sum) - (x_sum)**2)
a = y_mean - (b*x_mean)
print(f" b = {b} and a = {a}")

