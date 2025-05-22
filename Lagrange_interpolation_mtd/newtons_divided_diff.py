from math import prod

def p(X,xk,i):
    return prod(xk - X[j] for j in range(i))

def div_diff_table(X,Y):
    n = len(Y)
    D = [[0] * n for _ in range(n)]

    for i in range(n):
        D[i][0] = Y[i]

    for j in range( 1,n) :
        for i in range(n-j):
            D[i][j] = (D[i+1][j-1] - D[i][j-1]) / (X[i+j] - X[i])

        return [D[0][i] for i in range(n)]
    
def div_diff(data, xk):
    X = list(data.keys())
    Y = list(data.values())
    n = len(Y)

    divided_differences = div_diff_table(X,Y)
    return sum(divided_differences[i] * p(X,xk, i) for i in range(n))

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

print(div_diff(data, x_k))