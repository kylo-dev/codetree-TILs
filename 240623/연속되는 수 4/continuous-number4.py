n = int(input())

num_list = [int(input()) for _ in range(n)]

max_cnt = cur_cnt = 0

for i in range(n):
    if (i == 0 or num_list[i] > num_list[i-1]):
        cur_cnt += 1
    else:
        max_cnt = max(max_cnt, cur_cnt)
        cur_cnt = 1

print(max(max_cnt, cur_cnt))