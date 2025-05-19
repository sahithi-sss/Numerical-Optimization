#integration using romberg's integraation applied once
# f =  sinx ; x = 0 to 1; 10 intervals

import numpy as np

x1 = np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
y1 = np.zeros(11)

for i in range(0,len(x1)):
    y1[i] = np.sin(x1[i])
    #print(y[i])

h1 = 0.1
y1_sum= 0 
for i in range (1, 10):
   #print(x[i])
    y1_sum += y1[i]

ans1 = (h1/2) * (y1[0] + (2*y1_sum ) + y1[-1])
print(ans1)

x2 = np.arange(0, 1.0 + 0.05, 0.05)
#print(x2)
y2 = np.zeros(21)

for i in range(0,len(x2)):
    y2[i] = np.sin(x2[i])
    #print(y[i])

h2 = 0.05
y2_sum= 0 
for i in range (1, 20):
   #print(x[i])
    y2_sum += y2[i]

ans2 = (h2/2) * (y2[0] + (2*y2_sum ) + y2[-1])
print(ans2)

ans_final = ((4* ans2) - ans1) * (1/3)
print(ans_final)