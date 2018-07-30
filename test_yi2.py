__author__ = 'lenovo'
import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    try:
        while True:
            input_data = sys.stdin.readline().strip()
            if input_data == '':
                break
            len_b, a = input_data.split()
            a = int(a)
            len_b = int(len_b)
            for num in range(len_b):
                num = int(sys.stdin.readline().strip())
                if num > a:
                    a += gcd(num, a)
                else:
                    a += num
            print a
    except Exception:
        print('abb')
        pass
