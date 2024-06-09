n = int(input())

nums = [input() for _ in range(n)]

for i in sorted(nums):
    print(i)