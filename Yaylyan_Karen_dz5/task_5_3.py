def tic_tac_toe():
    field = [[' ']*3 for _ in range(3)]
    is_first = True

    while True:
        row, column = map(int, input('Введите номер строки и столбца через пробел: ').split())
        row -= 1
        column -= 1

        if field[row][column] != ' ':
            print('Это поле уже занято')
            continue


        if is_first:
            field[row][column] = 'X'
        else:
            field[row][column] = 'O'

        is_first = not is_first

        for i in range(len(field)):
            for j in range(len(field)):
                if j != 2:
                    print(field[i][j], end='| ')
                else:
                    print(field[i][j])
            print('-'*7)

        if (field[row][0] == field[row][1] == field[row][2] or
                field[0][column] == field[1][column] == field[2][column] or
                field[0][0] == field[1][1] == field[2][2] != ' ' or
                field[0][2] == field[1][1] == field[2][0] != ' '):
            print('Победа!')
            break

        if ' ' not in field[0] and ' ' not in field[1] and ' ' not in field[2]:
            print('Ничья!')
            break


tic_tac_toe()






    





