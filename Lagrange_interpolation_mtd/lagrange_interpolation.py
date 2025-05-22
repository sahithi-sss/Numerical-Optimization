from math import prod

def l( x,f,xk,i):
    n = len(x)
    return prod((xk-x[j])/(x[i] - x[j]) for j in range(n) if j != i)

def lagrange_interpolation(data, xk):
    x = list(data.keys())
    f = list(data.values())
    n = len(f)
    return sum( f[i] * l(x,f,xk,i) for i in range(n) )

data = {
1: 150.56000000,
2: 152.78000000,
3: 155.23000000,
4: 158.67000000,
5: 162.78000000,
6: 167.23000000,
7: 172.67000000,
8: 179.78000000,
9: 188.23000000,
10: 198.67000000
}

print(lagrange_interpolation(data,11))