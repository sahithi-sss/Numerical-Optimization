from math import factorial

def coeff(s,k):
    result = 1
    for i in range(k):
        result *= (s-i)
    return result/factorial(k)

def fwd_diff_table(Y):
    n = len(Y)
    F = [[0] * n for _ in range(n)]

    for i in range(n):
        F[i][0] = Y[i]

    for j in range(1,n):
        for i in range(n-j):
            F[i][j] = F[i+1][j-1] - F[i][j-1]

    return [F[0][i] for i in range(n)]

def fwd_diff(data, xk):
    X = list(data.keys())
    Y = list(data.values())
    n = len(X)

    h = X[1] - X[0]
    s = (xk - X[0]) / h

    fwd_differences = fwd_diff_table(Y)
    return sum(coeff(s,j) * fwd_differences[j] for j in range(n))

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

print(fwd_diff(data, x_k))