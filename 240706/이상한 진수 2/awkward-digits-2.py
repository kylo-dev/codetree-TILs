n = list(input())

for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
        break

num = ''.join(n)

print(int(num, 2))