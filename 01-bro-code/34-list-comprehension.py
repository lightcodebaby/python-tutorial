squares = []
for i in range(1, 11):
    squares.append(i * i)

print(squares)

squares = [i * i for i in range(1, 11)]
print(squares)

students_grades = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

passed_students = list(filter(lambda x: x >= 60, students_grades))

# or...

passed_students = [
    student_grade for student_grade in students_grades if student_grade >= 60
]

# or...

passed_students = [i if i >= 60 else "FAILED" for i in students_grades]
