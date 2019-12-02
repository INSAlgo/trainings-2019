from itertools import permutations
from numpy.random import permutation as permut
from taquin import start

number_iterations = int(input())
number_confirmed = 0
number_visited = [0 for k in range(number_iterations)]
while(number_confirmed != number_iterations):
    position_start = list(permut(9))
    print("pos start",position_start)
    res = start(position_start)
    if res!= -1:
        number_visited[number_confirmed] = res
        number_confirmed += 1
print(sum(number_confirmed)*1.0/number_iterations)