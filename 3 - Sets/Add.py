# Calculate the no of distinct countries among all the countries the stamps belong to

if __name__ == '__main__':
    n = int(input('Enter the no of stamps: '))
    stamps = set()
    for i in range(n):
        stamps.add(input('Enter the countries: '))
    print(len(stamps))
