from collections import deque

def negafibbo(k):
    if k == 0:
        return [0]

    result = deque([1, 0, 1])
    for i in range(1, k):
        result.appendleft(result[1] - result[0])
        result.append(result[-1] + result[-2])

    return list(result)


if __name__ == '__main__':
    k = int(input())
    print(negafibbo(k))
