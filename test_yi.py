__author__ = 'lenovo'


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    flag = True
    a = -1
    result = []
    while True:
        input_data = raw_input()
        if not input_data:
            break
        if flag:
            len_b, a = input_data.split()
            a = int(a)
            flag = False
        else:
            bn = list(input_data.split())
            bn = [int(num) for num in bn]
            for bi in bn:
                if bi > a:
                    a += gcd(bi, a)
                else:
                    a += bi
            result.append(a)
            flag = True
    else:
        pass
    for item in result:
        print item
