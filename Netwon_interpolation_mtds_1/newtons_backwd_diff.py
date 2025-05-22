from math import factorial

def coeff(s, j):
    result = 1
    for i in range(j):
        result *= (s+i)
    return result/ factorial(j)

def backward_diff_table(Y):
    n = len(Y)
    B = [[0] * n for _ in range(n)]

    for i in range(n):
        B[i][0] = Y[i]

    for j in range(1,n):
        for i in range(n-1,j-1,-1):
            B[i][j] = B[i][j-1] - B[i-1][j-1]
    
    return [B[n-1][j] for j in range(n)]

def backward_diff(data,xk):
    X = list(data.keys())
    Y = list(data.values())
    n = len(Y)

    h = X[1] - X[0]
    s = (xk - X[-1] ) / h

    backward_differences = backward_diff_table(Y)

    return sum(coeff(s,j) * backward_differences[j] for j in range(n))

data = {
  10: 12.34000000,
  20: 18.78000000,
  30: 25.56000000,
  40: 30.23000000,
  60: 34.56000000,
  70: 33.78000000,
  80: 29.45000000,
  90: 22.78000000,
  100: 15.23000000
}

x_k = 50

print(backward_diff(data, x_k))