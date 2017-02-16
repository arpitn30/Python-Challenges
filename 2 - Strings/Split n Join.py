# Split the given string on a " " (space) delimiter and join using a - hyphen.


def split_and_join(line):
    line = line.split(' ')
    return '-'.join(line)

if __name__ == '__main__':
    line = input('Enter String: ')
    result = split_and_join(line)
    print(result)
