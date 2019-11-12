n = int(input())
h = list(map(int, input().split()))
res_height = 0
for hi in h:
    res_height *= 2
    res_height += hi
p2 = pow(2, n)
res_energy = res_height // p2
if res_height % p2:
    res_energy += 1
print(res_energy)
