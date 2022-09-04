def del_all_substrings(line):
    inx = line.find('абв')
    while inx != -1:
        line = line[:inx] + line[inx+3:]
        inx = line.find('абв')

    return line


if __name__ == '__main__':
    line = input()
    print(del_all_substrings(line))
