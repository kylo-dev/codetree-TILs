binary = list(map(int, input()))
num = 0

for idx, val in enumerate(binary[::-1]):
    num += (2 ** idx) * val

print(num)