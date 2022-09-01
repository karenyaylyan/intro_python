def list_of_simple_multipliers(n):
    number = n
    result = []
    for i in range(2, n+1):
        while number % i == 0:
            result.append(i)
            number //= i
    return result


if __name__ == '__main__':
    N = int(input())
    print(list_of_simple_multipliers(N))
    