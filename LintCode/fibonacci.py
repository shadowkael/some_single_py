__author__ = 'lenovo'


def fibonacci(n):
    fibonacci_list = [0, 1]
    while n > len(fibonacci_list):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list[n - 1]