n = list(input())

flag = False

for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
        flag = True
        break

if not flag:
    for i in range(len(n), -1, -1):
        if n[i] == '1':
            n[i] = '0'
            break

num = ''.join(n)

print(int(num, 2))