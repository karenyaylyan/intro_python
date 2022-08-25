def diff_fract_part(arr):
    min_frac = max_frac = arr[0] - int(arr[0])

    for i in range(1, len(arr)):
        cur_frak = arr[i] - int(arr[i])

        if cur_frak > max_frac:
            max_frac = cur_frak

        if cur_frak < min_frac:
            min_frac = cur_frak

    return max_frac - min_frac


if __name__ == '__main__':
    arr = list(map(float, input().split()))
    print(diff_fract_part(arr))
