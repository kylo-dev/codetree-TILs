n = int(input())

def print_num(n, cnt):
    if (cnt > n):
        return
        
    print(cnt, end=" ")
    cnt += 1
    print_num(n, cnt)

def print_reverse(n):
    if (n == 0):
        return
    print(n, end=" ")
    print_reverse(n-1)

print_num(n, 1)
print()
print_reverse(n)