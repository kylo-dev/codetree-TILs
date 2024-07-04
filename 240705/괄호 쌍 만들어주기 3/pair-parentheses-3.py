st = input()

cnt = 0

for i in range(len(st)):

    if (st[i] == "("):
        for j in range(i+1, len(st)):
            if (st[j] == ")"):
                cnt += 1

print(cnt)