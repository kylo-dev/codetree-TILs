n = int(input())

square = [[0 for _ in range(201)] for _ in range(201)]

a_list = []
for _ in range(n):
    a_list.append(list(map(int, input().split())))

min_num = min(min(a[0], a[1], a[2], a[3]) for a in a_list)

if (min_num < 0):
    tol = abs(min_num)
    for a in a_list:
        a[0] += tol
        a[1] += tol
        a[2] += tol
        a[3] += tol

for a in a_list:
    for x in range(a[0], a[2]):
        for y in range(a[1], a[3]):
            square[x][y] = 1

result = 0
for s in square:
    result += sum(s)

print(result)