def test(num):
    for k in a:
        if(num % k != 0):
            return 0
    for k in b:
        if(k % num != 0):
            return 0
    return 1


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cpt = 0
for k in range(max(a), max(b)+1):
    cpt += test(k)
print(cpt)
