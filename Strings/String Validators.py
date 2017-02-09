# Display True if any of the character in the given string is validated

if __name__ == '__main__':
    s = input('Enter String: ')
    alnum, alpha, digit, lower, upper = False, False, False, False, False
    for i in range(len(s)):
        if s[i].isalnum():
            alnum = True
        if s[i].isalpha():
            alpha = True
        if s[i].isdigit():
            digit = True
        if s[i].islower():
            lower = True
        if s[i].isupper():
            upper = True

    print(alnum, alpha, digit, lower, upper, sep='\n')
