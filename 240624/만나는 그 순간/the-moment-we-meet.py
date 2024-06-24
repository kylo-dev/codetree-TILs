n, m = map(int, input().split())

n_list = [0]
m_list = [0]

for i in range(n):
    d, t = input().split()
    if d == 'R':
        for j in range(int(t)):
            n_list.append(n_list[-1] + 1)
    elif d == 'L':
        for j in range(int(t)):
            n_list.append(n_list[-1] - 1)

for i in range(m):
    d, t = input().split()
    if d == 'R':
        for j in range(int(t)):
            m_list.append(m_list[-1] + 1)
    elif d == 'L':
        for j in range(int(t)):
            m_list.append(m_list[-1] - 1)

check = False
for i in range(1, min(len(n_list), len(m_list))):
    if n_list[i] == m_list[i]:
        check = True
        print(i)
        break
    else:
        check = False

if not check:
    print(-1)