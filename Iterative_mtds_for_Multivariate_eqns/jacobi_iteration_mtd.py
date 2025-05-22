def jacobi_iteration(A,B,iter = 100):
    n = len(A)
    X = [0]* n

    for _ in range(iter):
        X_new = X.copy()

        for i in range(n):
            s = sum((A[i][j] * X[j]) for j in range(n) if j!=i)
            X_new[i] = (B[i] - s)/A[i][i]
        X = X_new

    return X

A = [[8, 3, -2],
	 [2, 10, 5],
	 [-3, 6, 15]]

B = [130, 250, 190]

print(jacobi_iteration(A,B,10))