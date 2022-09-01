def sum_of_odd(arr):
    result = 0
    for i in range(1, len(arr), 2):
        result += arr[i]

    return result


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(sum_of_odd(arr))
    