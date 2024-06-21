n = int(input())

cnt = 0 
cnt_list = []

num_list = [int(input()) for _ in range(n)]

for i in range(n):
    if (i == 0 or num_list[i] == num_list[i-1]):
        cnt += 1
    else:
        cnt_list.append(cnt)
        cnt = 1

print(max(cnt_list))