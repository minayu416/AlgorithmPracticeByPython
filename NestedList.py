students = []
s = set()
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append((name, score))
    s.add(score)

students = [("Harry", 37.21),("Berry", 37.21),("Tina", 37.2),("Akriti", 41),("Harsh", 39)]
second_low = sorted(s)
lowest = [student[0] for student in sorted(students, key=lambda student: student[1]) if student[1] == second_low]

for i in lowest:
    print(i)