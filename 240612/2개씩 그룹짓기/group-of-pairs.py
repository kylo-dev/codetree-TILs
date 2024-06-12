n = int(input())
nums = list(map(int, input().split()))

check = [sum(nums[i*n:i+n]) for i in range(len(nums)//n)]

print(max(check))