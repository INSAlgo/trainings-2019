n = int(input())
scores = list(map(int, input().split()))
ranks = [-1 for k in range(n)]
ranks[0] = 1
for k in range(1, n):
    if(scores[k] == scores[k - 1]):
        ranks[k] = ranks[k - 1]
    else:
        ranks[k] = ranks[k - 1] + 1
m = int(input())
l = list(map(int, input().split()))
s = 0
pos = n - 1
s = -1
for k in l:
    s = max(s, k)
    while s > scores[pos] and pos > 0:
        pos -= 1
    if s == scores[pos]: 
        print(ranks[pos])
    elif(s < scores[pos]):
        print(ranks[pos] + 1)
    else:
        print(ranks[pos])
