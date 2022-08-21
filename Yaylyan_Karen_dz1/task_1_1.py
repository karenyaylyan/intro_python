x, y = map(int, input().split())
if x == 0 and y == 0:
    print('Точка находится в начале координат')
elif x == 0:
    print('Точка находится на оси Y')
elif y == 0:
    print('Точка находится на оси X')
elif x > 0 and y > 0:
    print('Точка находится в 1 четверти')
elif x < 0 and y > 0:
    print('Точка находится во 2 четверти')
elif x < 0 and y < 0:
    print('Точка находится в 3 четверти')
elif x > 0 and y < 0:
    print('Точка находится в 4 четверти')