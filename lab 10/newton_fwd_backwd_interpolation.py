import numpy as np

x = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14, 15], dtype=float)  # Time (hours)
y = np.array([15.0, 15.9, 17.1, 18.2, 20.5, 21.8, 23.0, 24.1, 25.2, 25.9], dtype=float)  # Temperature (°C)

def fwd_diff_table(y):
    n = len(y)
    diff_table = np.zeros((n,n))
    diff_table[:,0] = y
    for j in range (1,n):
        for i in range (n-j):
            