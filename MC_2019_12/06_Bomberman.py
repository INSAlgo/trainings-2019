def print_grid(grid):
    for i in range(len(grid)):
        s = ""
        for x in grid[i]:
            s += "O" if x else "."
        print(s)


r, c, n = map(int, input().split())
n = n+1
if n <= 2:
    for k in range(r):
        print(input())
else:
    grid = [list(map(lambda x: 1 if x == 'O' else 0, input()))
            for _ in range(r)]
    if n % 2 == 1:
        print_grid([[1 for _ in range(c)] for _ in range(r)])
    else:

        memo = {str(grid): 2}
        reverse_memo = {2: grid}
        detect_cycle = 0
        len_cycle = -1
        ite = 2
        while not detect_cycle and ite < n:
            ite += 2
            copy_grid = [[0 for _ in range(c)] for _ in range(r)]
            for i in range(r):
                for j in range(c):
                    # put a bomb if no neighbour was one
                    put_bomb = 1
                    if grid[i][j]:
                        put_bomb = 0
                    elif i != 0 and grid[i-1][j]:
                        put_bomb = 0
                    elif j != 0 and grid[i][j-1]:
                        put_bomb = 0
                    elif i != r-1 and grid[i+1][j]:
                        put_bomb = 0
                    elif j != c-1 and grid[i][j+1]:
                        put_bomb = 0
                    copy_grid[i][j] = put_bomb
            key_str = str(copy_grid)
            if key_str in memo:
                len_cycle = ite - memo[key_str]
                detect_cycle = 1
                start_cycle = memo[key_str]
            else:
                memo[key_str] = ite
                reverse_memo[ite] = copy_grid.copy()
            grid = copy_grid.copy()
        result_index = n
        if len_cycle != -1:
            result_index = ((n - start_cycle) % len_cycle) + start_cycle
        print_grid(reverse_memo[result_index])
