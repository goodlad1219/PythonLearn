if __name__ == '__main__':
    list1 = []
    N = int(input())
    for i in range(N):
        command = input()
        
        cmd = command.lower().split()
        if (cmd[0] == 'insert'):
            list1.insert(int(cmd[1]),int(cmd[2]))
        elif (cmd[0] == 'print'):
            print (list1)
        elif (cmd[0] == 'remove'):
            list1.remove(int(cmd[1]))
        elif (cmd[0] == 'append'):
            list1.append(int(cmd[1]))
        elif (cmd[0] == 'sort'):
            list1.sort()
        elif (cmd[0] == 'pop'):
            list1.pop()
        elif (cmd[0] == 'reverse'):
            list1.reverse()