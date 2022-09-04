def candy_game(candy_count, max_step_count, is_bot):
    print(f'Всего конфет: {candy_count}, максимум можно взять: {max_step_count}')
    is_first = True
    while candy_count > 0:
        if is_first:
            step_count = int(input('Первый игрок берет конфеты: '))
        elif is_bot:
            step_count = candy_count % (max_step_count + 1)
            if step_count == 0:
                step_count = 1
            print(f'Бот взял {step_count} конфет')
        else:
            step_count = int(input('Второй игрок берет конфеты: '))

        if step_count < 0 or step_count > max_step_count or step_count > candy_count:
            print('Неверное число конфет. Введите еще раз')
            continue

        candy_count -= step_count
        is_first = not is_first
        print(f'Осталось конфет: {candy_count}')

    if is_first and not is_bot:
        print('Второй игрок победил')
    elif is_first:
        print('Бот победил')
    else:
        print('Первый игрок победил')

if __name__ == '__main__':
    candy_game(202, 28, False)

