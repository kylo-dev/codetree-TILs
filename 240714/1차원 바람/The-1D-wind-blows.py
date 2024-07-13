n, m, q = map(int, input().split())

arr = [
    [0 for _ in range(m+1)]
    for _ in range(n+1)
]

def shift(row, direct):
    if direct == 'R':
        arr[row].insert(1, arr[row].pop())
    elif direct == 'L':
        arr[row].insert(m, arr[row].pop(1))

def has_same_number(row1, row2):
    return any([
        arr[row1][col] == arr[row2][col]
        for col in range(1, m+1)
    ])

def flip(curr_dir):
    return 'L' if curr_dir == 'R' else 'R'

def simulate(start_row, start_dir):

    shift(start_row, start_dir)
    start_dir = flip(start_dir)

    curr_dir = start_dir
    for row in range(start_row, 1, -1):
        if has_same_number(row, row-1):
            shift(row-1, curr_dir)
            curr_dir = flip(curr_dir)
        else:
            break
    
    curr_dir = start_dir
    for row in range(start_row, n):
        if has_same_number(row, row+1):
            shift(row+1, curr_dir)
            curr_dir = flip(curr_dir)
        else:
            break

for row in range(1, n+1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start=1):
        arr[row][col] = num

for _ in range(q):
    r, d = tuple(input().split())
    r = int(r)

    simulate(r, flip(d))

for row in range(1, n+1):
    for col in range(1, m+1):
        print(arr[row][col], end=' ')
    print()