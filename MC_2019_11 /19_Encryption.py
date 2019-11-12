import math
s = input().replace(" ", "")
row = math.floor(pow(len(s), 0.5))
col = math.floor(pow(len(s), 0.5))
if(row * col < len(s)):
    col += 1
if(row * col < len(s)):
    row += 1
grid = [['' for i in range(col)] for j in range(row)]
for k in range(len(s)):
    grid[(k // col)][k % col] = s[k]
res = ""
for i in range(col):
    for j in range(row):
        if(grid[j][i] != ''):
            res += grid[j][i]
    res += " "
print(res[:-1])
