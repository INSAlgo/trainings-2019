q = int(input())
values = [int(input()) for k in range(q)]
maxi = max(values) + 1
mem = [float('inf')] * maxi
mem[0] = 0
for i in range(maxi-1):
    mem[i+1] = min(mem[i+1], mem[i] + 1)
    for j in range(i+1):
        if i*j >= maxi:
            break
        mem[i*j] = min(mem[i*j], mem[i] + 1)
for val in values:
    print(mem[val])
