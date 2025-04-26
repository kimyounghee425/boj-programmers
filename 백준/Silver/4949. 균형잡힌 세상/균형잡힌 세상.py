while True :
    a = input()
    s = []
    if a=='.':
        break
    for i in a :
        if i == '[' or i == '(' :
            s.append(i)
        elif i == ']' :
            if s and s[-1] == '[' :
                s.pop() 
            else : 
                s.append(i)
                break
        elif i == ')' :
            if s and s[-1] == '(' :
                s.pop()
            else :
                s.append(i)
                break
    if not s :
        print('yes')
    else :
        print('no')