# Program to hash a tuple of integers which are given as input


if __name__ == '__main__':
    n = int(input('Enter no of integers: '))
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
