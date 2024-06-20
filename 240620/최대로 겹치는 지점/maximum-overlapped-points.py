n = int(input())

leng = [0 for _ in range(101)]

a_list = []
for _ in range(n):
    a_list.append(list(map(int, input().split())))

for a in a_list:
    for j in range(a[0], a[1] + 1):
        leng[j] += 1

print(max(leng))