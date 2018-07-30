I = 1


def get_prime_num(num_list, edge):
    for i in num_list:
        if edge % i == 0:
            break
    else:
        num_list.append(edge)
        global I
        I = 1


def generate_num(num_list, num):
    while len(num_list) < num:
        global I
        get_prime_num(num_list, num_list[-1] + I)
        I += 1
    else:
        print(num_list[-1])
    print(num_list)


if __name__ == "__main__":
    generate_num([2], 1000)
