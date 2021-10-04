# Program to find the second largest number in the list


if __name__ == '__main__':
    n = int(input('Enter no of integers: '))
    arr = map(int, input().split())
    maxi2 = sorted(arr)[-2]
    print(maxi2, end="\n")
