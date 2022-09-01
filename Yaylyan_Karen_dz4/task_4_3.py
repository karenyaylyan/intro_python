from random import randint

def mnogochlen(k):
    indexes = {"0": "\u2070",
               "1": "\u00B9",
               "2": "\u00B2",
               "3": "\u00B3",
               "4": "\u2074",
               "5": "\u2075",
               "6": "\u2076",
               "7": "\u2077",
               "8": "\u2078",
               "9": "\u2079",
               "-": "\u207B"
           }

    arr = []
    for i in range(k+1):
        koef = randint(0, 100)
        if koef > 0:
            if i != k:
                k_string = str(k-i)
                if k_string == '1':
                    arr.append(f'{koef}*x')
                    continue

                stepen = ''
                for c in k_string:
                    stepen += indexes[c]
                arr.append(f'{koef}*x{stepen}')
            else:
                arr.append(f'{koef}')

    result = ''
    for i in range(len(arr)):
        if i != len(arr) - 1:
            result += arr[i] + ' + '
        else:
            result += arr[i] + ' = 0'

    return result


if __name__ == '__main__':
    k = int(input())

    with open('file.txt', 'w') as ouf:
        ouf.write(mnogochlen(k))
