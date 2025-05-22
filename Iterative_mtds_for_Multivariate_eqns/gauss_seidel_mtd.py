def gauss_seidel(A,B,iter = 100):
    n = len(A)
    X = [0]* n

    for _ in range(iter):
        for i in range(n):
            s = sum((A[i][j] * X[j]) for j in range(n) if i != j)
            X[i] = (B[i] - s) / A[i][i]

    return X

A = [[8, 3, -2],
	 [2, 10, 5],
	 [-3, 6, 15]]

B = [130, 250, 190]

print(gauss_seidel(A,B,10))