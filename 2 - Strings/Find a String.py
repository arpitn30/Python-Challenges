# Count the number of substring occurrences  in the given string


def count_substring(string, sub_string):
    i = 0
    pos = list()
    while i < len(string):
        i = string.find(sub_string, i)
        if i == -1:
            break
        pos = pos + [i]
        i += 1
    return len(pos)


if __name__ == '__main__':
    string = input().strip('Enter Text: ')
    sub_string = input().strip('Enter substring to find: ')

    count = count_substring(string, sub_string)
    print(count)
