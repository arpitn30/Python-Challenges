# A set is an unordered collection of elements without duplicate entries.
# When printed, iterated or converted into a sequence, its elements will appear in an random order.
# Print the avg of the distinct elements of all the elements given by the user


def average(array):
    distinct = set(arr)
    add = sum(distinct)
    length = len(distinct)
    return add / length

if __name__ == '__main__':
    n = int(input('Enter no of elements: '))
    arr = list(map(int, input('Enter Elements: ').split()))
    result = average(arr)
    print(result)
