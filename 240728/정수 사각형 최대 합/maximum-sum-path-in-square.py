n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_max_sum(x, y, sum):
    global max_sum

    if x == n - 1 and y == n - 1:
        max_sum = max(max_sum, sum)
        return
    
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if in_range(new_x, new_y):
            find_max_sum(new_x, new_y, sum + arr[new_x][new_y])

find_max_sum(0, 0, arr[0][0])

print(max_sum)