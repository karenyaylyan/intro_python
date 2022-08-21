number_of_quarter = int(input())
if number_of_quarter == 1:
    print('x > 0, y > 0')
elif number_of_quarter == 2:
    print('x < 0, y > 0')
elif number_of_quarter == 3:
    print('x < 0, y < 0')
elif number_of_quarter == 4:
    print('x > 0, y < 0')
else:
    raise ValueError('Допустимые значения для четвертей: 1-4')