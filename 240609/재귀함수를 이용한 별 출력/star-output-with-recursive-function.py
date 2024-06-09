n = int(input())

def print_star(n, cnt):
    if (cnt > n):
        return
    
    print("*" * cnt)
    cnt += 1
    print_star(n, cnt)

print_star(n, 1)