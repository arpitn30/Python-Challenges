# Program to find the second largest number in the list


if __name__ == '__main__':
    n = int(input('Enter no of integers: '))
    arr = map(int, input().split())
    maxi = max(arr)

    maxi2 = -999
    for i in arr:
        if maxi2 < i < maxi:
            maxi2 = i
    print(maxi2, end="\n")
