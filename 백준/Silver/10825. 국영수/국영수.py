import sys

class Info:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.mat = int(mat)

students = []

for _ in range(int(sys.stdin.readline())):
    name, kor, eng, mat = sys.stdin.readline().split()
    student = Info(name, kor, eng, mat)
    students.append(student)

students.sort(key=lambda student: (-student.kor, student.eng, -student.mat, student.name))

for student in students:
    print(student.name)