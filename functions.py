def read_file(file_name, list_of_numbers):
    with open(file_name) as f:
        for line in f:
            list_of_numbers += [float(x) for x in line.split()]
    return list_of_numbers


def minimum(list_of_numbers):
    min_value = float('inf')
    for i in list_of_numbers:
        if i < min_value:
            min_value = i
    return min_value


def maximum(list_of_numbers):
    max_value = float('-inf')
    for i in list_of_numbers:
        if i > max_value:
            max_value = i
    return max_value


def s(list_of_numbers):
    s = 0
    for i in list_of_numbers:
        s += i
    return s


def p(list_of_numbers):
    p = 1
    for i in list_of_numbers:
        try:
            p *= i
        except OverflowError:
            print('Возникла ошибка переполнения')
            raise
    return p
