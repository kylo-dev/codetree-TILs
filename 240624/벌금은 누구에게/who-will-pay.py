n, m, k = map(int, input().split())

m_list = [0] * (n+1)

for i in range(m):
    num = int(input())
    m_list[num] += 1

    if m_list[num] >= k:
        print(num)

if (max(m_list) > k):
    print(-1)