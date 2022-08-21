def mul_numbers(N):
    arr = [1]
    for i in range(1, N):
        arr.append((i+1)*arr[-1])
    return arr


if __name__ == '__main__':
    N = int(input())
    print(mul_numbers(N))
