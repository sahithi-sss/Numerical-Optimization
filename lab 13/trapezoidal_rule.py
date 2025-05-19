#integration using composite trapezoidal rule
# f =  sinx ; x = 0 to 1; 10 intervals

import numpy as np

x = np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
y = np.zeros(11)

for i in range(0,len(x)):
    y[i] = np.sin(x[i])
    #print(y[i])

h = 0.1
y_sum= 0 
for i in range (1, 10):
   #print(x[i])
    y_sum += y[i]

ans = (h/2) * (y[0] + (2*y_sum ) + y[-1])
print(ans)