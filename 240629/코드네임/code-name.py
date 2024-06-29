name_list = [input().split() for _ in range(5)]

name_list = sorted(name_list, key=lambda x: int(x[1]))

print(' '.join(name_list[0]))