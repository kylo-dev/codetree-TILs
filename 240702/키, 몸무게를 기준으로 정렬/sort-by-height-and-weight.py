n = int(input())

n_list = [input().split() for _ in range(n)]

n_list.sort(key = lambda x: (int(x[1]), -int(x[2])))

for name, hei, wei in n_list:
    print(name, hei, wei)