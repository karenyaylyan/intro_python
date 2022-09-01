def convert_decimal_to_binary(number):
    result = ''
    if number == 0:
        return '0'

    while number > 0:
        result = str(number % 2) + result
        number //= 2

    return result


def convert_with_bin_func(number):
    return bin(number)[2:]

if __name__ == '__main__':
    number = int(input())
    print(convert_decimal_to_binary(number))
    print(convert_with_bin_func(number))
