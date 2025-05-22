import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([25.0,27.2,30.1,33.8,38.2,43.4,49.3,56.1,63.7,72.1,81.4,91.5,102.5])
#print(len(x))
#print(len(y))

#rate at t=0 using 2 point fwd diff
h1 = 1
ans1 = (y[1] - y[0]) / h1
print(ans1)

# 3point fwd diff
h1 = 1
ans2 = (-(3*y[0]) + (4 * y[1]) - y[2]) /  (2*h1)
print(ans2)

#plot
plt.plot(x,y)
plt.xlabel("time")
plt.ylabel("temp")
plt.grid()
plt.show()

#2 point backward diff at t = 3
h2 = 1
ans5 = (y[3] - y[2]) / (h2)
print(ans5)

#3 point backward diff at t= 3
h2 = 1
ans3 = ((3* y[3]) - (4*y[2]) + y[1]) / (2* h2)
print(ans3)

#2 point central diff at t=2
h3 = 1
ans6 = (y[3] - y[1])/ (2*h3)
print(ans6)

#double diff - 3 point central at t = 2
h3 = 1
ans4 = (y[3] - (y[2]) + y[1]) / (h3 * h3)
print(ans4)