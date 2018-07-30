__author__ = 'lenovo'
import sys

if __name__ == "__main__":
    try:
        while True:
            input_data = sys.stdin.readline().strip()
            if input_data == '':
                break
            num = int(input_data)
            cow_ais = sys.stdin.readline().strip().split()
            cow_ais = [int(cow_ai) for cow_ai in cow_ais]
            if sum(cow_ais) % num != 0:
                print -1
            else:
                average = sum(cow_ais) / num
                count = 0
                for cow_ai in cow_ais:
                    if (cow_ai - average) % 2 != 0:
                        print -1
                        break
                else:
                    for cow_ai in cow_ais:
                        if cow_ai > average:
                            count += (cow_ai - average) / 2
                    print count

    except Exception:
        pass
