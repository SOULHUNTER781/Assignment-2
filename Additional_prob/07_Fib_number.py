import numpy as np
def matrix_mul(A,B):
    C = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k]*B[k][j]
    return C

def fib(n):
    A = [[1,1],[1,0]]
    R = [[1,0],[0,1]]
    while n != 0:
        if n % 2 == 1:
            R = matrix_mul(R,A)
        A = matrix_mul(A,A)
        n //= 2
    return R[1][0]

n = int(input())
print(fib(n))



