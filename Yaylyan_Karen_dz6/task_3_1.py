def sum_of_odd(arr):
    return sum([arr[i] for i in range(len(arr)) if i % 2])

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(sum_of_odd(arr))
