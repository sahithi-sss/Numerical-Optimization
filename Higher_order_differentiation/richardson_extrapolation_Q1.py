import numpy as np

x = np.array([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4])
y = np.array([12000,11980,11959,11936,11910,11885,11857,11828,11800,11769,11740,11710,11679])
#print(len(x))
#print(len(y))

i1 = np.where(x == 1.2)
#print(i1)

h1 = 0.4
ans1 = (y[8] - y[6]) * 1/h1
print(ans1)

h2 = 0.2
ans2 = (y[7] - y[6]) * 1/h2
print(ans2)

#richardson interpolation
ans3 = ((4*ans2) - ans1) / 3
print(ans3)

#err wrt basic fininte diff
err1 = ans3 - ans1
print(err1)

err2 = ans3 - ans2
print(err2)

#assuming const vel = ans3
alt_diff = ans3 * 0.2
alt = y[6] + alt_diff
print(alt)
err3 = alt - y[7]
print(err3)
