# students with index numbers:
student = ["john", "mark", "vanessa", "mariam"]

for index, student in enumerate(student):   # (student, 1) : starts with 1
    print(index, student)

#


students = ["john", "mark", "vanessa", "mariam"]

A = []
B = []
for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print("A :", A)
print("B :", B)

#

# MULAKAT SORUSU


students = ["john", "mark", "vanessa", "mariam"]
def divide_students(students):
    student_group = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            student_group[0].append(student)
        else:
            student_group[1].append(student)
    print(student_group)
    return student_group

st = divide_students(students)
st[0]
st[1]
# [['john', 'vanessa'], ['mark', 'mariam']]







