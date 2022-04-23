while(True):
    print(":>>> ",end = "")
    command  = input()
    li = command.split()
    if li[0] == 'quit':
        quit()
    elif li[0] == 'print':
        for i in li[1:]:
            print(i + " ",end = "" )
        print()
    elif li[0] == 'add':
        sum = 0
        for i in li[1:]:
            sum += int(i)
        print(sum)
    else:
        pass