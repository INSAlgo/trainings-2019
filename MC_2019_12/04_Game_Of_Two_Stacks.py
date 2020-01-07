for _ in range(int(input())):
    n, m, x = map(int, input().split())
    sA = list(map(int, input().split()))
    sB = list(map(int, input().split()))
    sumA = [0] * (n + 1)
    sumB = [0] * (m + 1)
    for k in range(1, n + 1):
        sumA[k] = sumA[k-1] + sA[k-1]
    for k in range(1, m + 1):
        sumB[k] = sumB[k-1] + sB[k-1]
    ptA = 0
    ptB = m
    best = 0
    while(ptA <= n and sumA[ptA] <= x):
        if sumA[ptA] + sumB[ptB] <= x:
            best = max(best, ptA+ptB)
            ptA += 1
        else:
            if ptB != 0:
                ptB -= 1
    print(best)
