a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(sum(a)/len(a), sum(b)/len(b))

for i in range(4):
    print((a[i]+b[i])/2, end=' ')

print()
print(round((sum(a)+sum(b))/(len(a)+len(b)),1))