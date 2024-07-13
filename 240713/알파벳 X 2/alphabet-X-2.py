n = input()

positions = {}
for idx, char in enumerate(n):
    if char in positions:
        positions[char].append(idx)
    else:
        positions[char] = [idx]

segments = []
for char, pos in positions.items():
    if len(pos) == 2:
        segments.append((pos[0], pos[1]))

def is_middle(seg1, seg2):
    a, b = seg1
    c, d = seg2

    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    return (a<c<b<d) or (c<a<d<b)

cnt = 0

for i in range(len(segments)):
    for j in range(i+1, len(segments)):
        if is_middle(segments[i], segments[j]):
            cnt += 1

print(cnt)