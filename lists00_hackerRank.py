if __name__ == '__main__':
    N = int(raw_input())
    result_list = []
    mycode = ""

    for _ in range(N):
        #raw_input() get everything on the line, the command and its argument(s)
        name = raw_input()
        # List that contain values of name
        x = name.split()

        # 3 cas : longueur 1 = print,pop & co longueur 2 = append ou remove et longueur 3
        # vaut pour insert
        # print, pop, sort or reverse
        if(len(x) == 1):
            if(x[0] == 'print'):
                print(result_list)
            else:
                exec("result_list."+str(x[0])+"()")
        #append and remove
        elif(len(x) == 2):
            arg1 = str(x[1])
            code = str(x[0])
            exec("result_list."+code+"("+arg1+")")
        #insert
        else:
            result_list.insert(int(x[1]), int(x[2]))


