# A and B are two disjoint sets. Analyse given array and calculate total happiness

if __name__ == '__main__':
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    like = set(map(int, input().split()))
    hate = set(map(int, input().split()))

    result = 0
    for i in arr:
       if i in like:
           result += 1
       elif i in hate:
           result -= 1
       else:
           pass
    print(result)
