def func(list, cmnd):
    if(cmnd[0] == "insert"):
        list.insert(int(cmnd[1]), int(cmnd[2]))
    elif (cmnd[0] == "print"):
        print list
    elif (cmnd[0] == "remove"):
        list.remove(int(cmnd[1]))
    elif (cmnd[0] == "append"):
        list.append(int(cmnd[1]))
    elif(cmnd[0] == "sort"):
        list.sort()
    elif(cmnd[0] == "pop"):
        list.pop()
    elif(cmnd[0] == "reverse"):
        list.reverse()
    else:
        print "Wrong Command\n"



if __name__ == '__main__':
    list = []
    N = int(raw_input())
    for i in range(N):
        inp = raw_input()
        #print inp
        cmnd = inp.split()
        func(list, cmnd)