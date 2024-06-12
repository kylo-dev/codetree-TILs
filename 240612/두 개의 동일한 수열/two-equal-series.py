n = int(input())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

if len(set(a_list) - set(b_list)) == 0:
    print("Yes")
else:
    print("No")