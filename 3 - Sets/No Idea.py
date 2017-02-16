# A and B are two disjoint sets. Analyse given array and calculate total happiness

if __name__ == '__main__':
    m, n = map(int, input('Enter no of elements for the array and disjoint sets: ').split())
    arr = list(map(int, input('Enter array: ').split()))
    like = set(map(int, input('Enter elements you like: ').split()))
    hate = set(map(int, input('Enter elements you don\'t like').split()))

    result = 0
    for i in arr:
       if i in like:
           result += 1
       elif i in hate:
           result -= 1
       else:
           pass
    print(result)
