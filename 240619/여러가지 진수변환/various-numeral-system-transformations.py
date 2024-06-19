def sol(n, q):
    result = ""

    while (n > 0):
        n, mod = divmod(n ,q)
        result += str(mod)
    
    return result

n, q = map(int, input().split())
result = sol(n, q)
print(result[::-1])