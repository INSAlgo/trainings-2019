n = int(input())
matrix = [list(map(int, input().split())) for k in range(n)]
diag = [0, 0]
for k in range(n):
    diag[0] += matrix[k][k]
    diag[1] += matrix[k][n - 1 - k]
print(abs(diag[0] - diag[1]))