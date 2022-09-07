def del_words(text, word):
    arr = text.split()
    arr = filter(lambda x: word not in x, arr)
    return ' '.join(arr)


if __name__ == '__main__':
    text = input()
    print(del_words(text, 'абв'))

