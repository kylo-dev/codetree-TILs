n = int(input())

max_cnt = cur_cnt = 0

num_list = [int(input()) for _ in range(n)]

for i in range(n):
    if (i == 0 or (num_list[i] > 0 and num_list[i-1] > 0)):
        cur_cnt += 1
    elif (num_list[i] < 0 and num_list[i-1] < 0):
        cur_cnt += 1
    else:
        max_cnt = max(max_cnt, cur_cnt)
        cur_cnt = 1

print(max(max_cnt, cur_cnt))