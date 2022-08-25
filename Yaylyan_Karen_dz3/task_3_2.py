def mul_pairs_of_list(arr):
    result = []
    for i in range(len(arr) // 2):
        result.append(arr[i] * arr[len(arr) - i - 1])

    if len(arr) % 2 == 1:
        result.append(arr[len(arr) // 2] * arr[len(arr) // 2])

    return result


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(mul_pairs_of_list(arr))
