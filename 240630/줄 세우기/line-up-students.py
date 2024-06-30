class Student:
    def __init__(self, height, weight, number):
        self.height, self.weight, self.number = height, weight, number

n = int(input())
students = []

for i in range(1, n+1):
    height, weight = map(int, input().split())
    students.append(Student(height, weight, i))

students.sort(key=lambda x: (-x[0], -x[1], x[2]))

for student in students:
    print(student.height, student.weight, student.number)