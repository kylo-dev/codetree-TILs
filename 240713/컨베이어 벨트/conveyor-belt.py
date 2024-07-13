n, t = map(int, input().split())

se = [list(map(int, input().split())) for _ in range(2)]
se = se[0] + se[1]

for _ in range(t):
    se = se[-1:] + se[:-1] 
    

for i in range(len(se)):
    if (i == 3):
        print()
    print(se[i], end=" ")