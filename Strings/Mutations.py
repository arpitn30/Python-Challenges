# Since strings are immutable, this function changes the specified character in the given string

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    # Or can be done by type casting to list and using join after changing the character
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
