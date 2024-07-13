n, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]
arr = arr[0] + arr[1] + arr[2]

for _ in range(t):
    arr = arr[-1:] + arr[0:-1]

for i in range(n*3):
    if i % n == 0 and i != 0:
        print()
    print(arr[i], end=' ')