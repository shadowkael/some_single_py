import sys

for line in sys.stdin:
    a = line.split()
    num = int(a[0])
    students = [int(student) for student in a[1]]
    k = int(a[2].split()[0])
    gap = int(a[2].split()[1])

    if gap >= num:
        students.sort(reverse=True)
        max_power = 1
        for student in students[:k]:
            max_power *= student
        print max_power



