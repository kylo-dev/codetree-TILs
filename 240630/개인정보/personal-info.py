students = [input().split() for _ in range(5)]

print("name")
students.sort(key = lambda x: x[0])
for st in students:
    print(' '.join(st))

print()

print("height")
students.sort(key = lambda x: -int(x[1]))
for st in students:
    print(' '.join(st))