# Program to take commands from user and implement list functions as requested


def func(list, cmnd):
    """Implement list functions using arguments from the user"""
    if cmnd[0] == "insert":
        list.insert(int(cmnd[1]), int(cmnd[2]))
    elif cmnd[0] == "print":
        print(list,end="\n")
    elif cmnd[0] == "remove":
        list.remove(int(cmnd[1]))
    elif cmnd[0] == "append":
        list.append(int(cmnd[1]))
    elif cmnd[0] == "sort":
        list.sort()
    elif cmnd[0] == "pop":
        list.pop()
    elif cmnd[0] == "reverse":
        list.reverse()
    else:
        print("Wrong Command\n")

if __name__ == '__main__':
    lst = []
    N = int(input("Enter no of commands: "))
    for i in range(N):
        inp = input("Enter command: ")
        cmnd = inp.split()
        func(lst, cmnd)