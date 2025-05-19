#integration using composite simpson 3/8rds rule
# f =  sinx ; x = 0 to 1; 10 intervals ; n = even

import numpy as np

x = np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
y = np.zeros(11)

for i in range(0,len(x)):
    y[i] = np.sin(x[i])
    #print(y[i])

h = 0.1

y_sum_1= 0
y_sum_2= 0 
for i in range (1, 10):
    if (i%3 != 0):
        #print(x[i])
        y_sum_1 += y[i]
    else:
        #print("x")
        #print(x[i])
        y_sum_2 += y[i]

ans = (h*(3/8)) * (y[0] + (3* y_sum_1) + (2 * y_sum_2) + y[-1])
print(ans)