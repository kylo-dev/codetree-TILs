n = int(input())

n_list = [input().split() for _ in range(n)]

n_list.sort(key = lambda x: int(x[1]))

for i in n_list:
    print(' '.join(i))