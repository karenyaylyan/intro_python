def sum_of_digits(number):
    result = 0
    for x in number:
        if ord('0') <= ord(x) <= ord('9'):
            result += ord(x) - ord('0')
        elif x != ',' and x != '-':
            raise ValueError('Введено не вещественное число')
    return result

if __name__ == '__main__':
    number = input()
    print(sum_of_digits(number))