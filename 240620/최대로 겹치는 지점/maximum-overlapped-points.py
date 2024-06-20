n = int(input())

leng = [0 for _ in range(201)]

a_list = []
for _ in range(n):
    a_list.append(list(map(int, input().split())))

min_num = min(min(a[0], a[1]) for a in a_list)

if (min_num < 0):
    tol = abs(min_num)
    for a in a_list:
        a[0] += tol
        a[1] += tol

for a in a_list:
    for j in range(a[0] + 1, a[1] + 1):
        leng[j] += 1

print(max(leng))