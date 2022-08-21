from random import randint

def shuffle_list(arr):
    for i in range(len(arr)):
        j = randint(0, len(arr)-1)
        arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    shuffle_list(arr)
    print(arr)