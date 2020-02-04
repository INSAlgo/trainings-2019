n, k = map(int, input().split())
l = list(map(lambda x: int(x) % k, input().split()))
r = [0]*k
for i in l:
    r[i] += 1
cpt = 0
if(r[0] != 0):
    cpt += 1
if(k % 2 == 1):
    for i in range(1, (k+1)//2):
        cpt += max(r[i], r[k-i])
else:
    for i in range(1, (k)//2):
        cpt += max(r[i], r[k-i])
    if(r[k//2] != 0):
        cpt += 1
print(cpt)
