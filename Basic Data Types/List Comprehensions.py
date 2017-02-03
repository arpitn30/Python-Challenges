# Program to print a list of all possible coordinates given by i, j, k  on a 3D grid
# where the sum of i + j + k is not equal to N.

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    coords = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n]
    coords = sorted(coords)
    print(coords)
