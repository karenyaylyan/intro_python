def unique_numbers(arr):
    result = []
    s = set()
    for el in arr:
        if el not in s:
            s.add(el)
            result.append(el)
    return result

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(unique_numbers(arr))