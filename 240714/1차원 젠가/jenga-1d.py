n = int(input())
arr = [int(input()) for _ in range(n)]

for _ in range(2):
    s1, e1 = map(int, input().split())
    for j in range(s1, e1+1):
        arr[j-1] = 0
    tmp = [i for i in arr if i != 0]
    arr = tmp

print(len(arr))
for i in arr:
    print(i)