import sys

if __name__ == "__main__":
    try:
        while True:
            input_data = sys.stdin.readline().strip()
            if input_data == '':
                break
            num = int(input_data)
            students = sys.stdin.readine().strip()
            students = [int(student) for student in students]
            third = sys.stdin.readline().strip().split()
            k = int(third[0])
            gap = int(third[1])

            students.sort(reverse=True)
            max_power = 1
            for student in students[:k]:
                max_power *= student
                print max_power
    except:
        pass
