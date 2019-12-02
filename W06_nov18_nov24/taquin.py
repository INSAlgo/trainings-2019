from collections import defaultdict
from heapq import heappush, heappop

def check_final_position(position):
    for square in range(9):
        if position[square] != square:
            return False
    return True

def gen_key_from_array(position):
    key = 0
    pow10 = 1
    for digit in position[::-1]:
        key += digit * pow10
        pow10*=10
    return key

def gen_array_from_key(key):
    array = list(str(key))
    if len(array) != 9:
        array = [0] + array
    return array

def switch_empty(position, pos_empty, diff):
    neigh = position.copy()
    neigh[pos_empty] = neigh[pos_empty+diff]
    neigh[pos_empty+diff] = 0
    return neigh

def generate_neighbors(position):
    neighbors = []
    pos_empty = position.index(0)
    if pos_empty%3 != 0:
        # move empty square to the left
        neighbors.append(switch_empty(position,pos_empty,-1))
    if pos_empty%3 != 2:
        # move empty square to the right
        neighbors.append(switch_empty(position,pos_empty,1))

    if pos_empty >= 3:
        # move empty square up
        neighbors.append(switch_empty(position,pos_empty,-3))

    if pos_empty <= 5:
        # move empty square down
        neighbors.append(switch_empty(position,pos_empty,3))
    return neighbors

def heuristic(position):
    return less_dumb_heuristic(position)

def dumb_heuristic(position):
    return 0

def less_dumb_heuristic(position):
    dist = 0
    for k in range(9):
        if position[k] != k:
            dist += 1
    return dist

def start(position_start):
    visited = defaultdict(lambda : False)
    waiting_list = [(heuristic(position_start),position_start,0)]
    min_confirmed = -1
    search_ended = 0
    # explore all configurations from the start
    number_explored = 0
    while not search_ended and waiting_list:
        print(number_explored,len(waiting_list))
        # get the element with the best heuristic in the heap
        heuristic_state, state, cost = heappop(waiting_list)
        # if it is the end position, return it
        if check_final_position(state):
            search_ended = 1
            min_confirmed = cost
        key = gen_key_from_array(state)
        if not visited[key]: # check that this element has not already been explored
            number_explored +=1

            # explore neighbors
            neighbors = generate_neighbors(state)
            for neigh in neighbors:
                key_neigh = gen_key_from_array(neigh) # check that they are not already discovered
                if not visited[key_neigh]:
                    cost_heuristic = cost + heuristic(neigh)
                    heappush(waiting_list,(cost_heuristic,neigh,cost+1))
    if not search_ended:
        print("NO SOLUTIONS")
    print("number explored : ",number_explored)
    return min_confirmed
# init_pos = [1,2,5,0,3,4,6,7,8]    
# print(start(init_pos))