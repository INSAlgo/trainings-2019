n, d = map(int, input().split())
a = list(map(int, input().split()))
a = a[d % n:] + a[:d % n]
print(" ".join(map(str, a)))
