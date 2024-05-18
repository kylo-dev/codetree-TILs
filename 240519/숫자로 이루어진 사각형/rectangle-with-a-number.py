n = int(input())

for i in range(n):
    for j in range(n):
        print((i * n + j) % 9 + 1, end=' ')
    print()