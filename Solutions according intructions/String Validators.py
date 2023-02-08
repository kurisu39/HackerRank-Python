if __name__ == '__main__':
    s = input()
    
    lst=list(s)
    lst,list()

    a=""
    b=""
    c=""
    d=""
    e=""
    
    for z in range (0,len(lst)):
        print (lst[0])
        if lst[0].isalnum()==True:
            a="True"
            break
        else:
            a="False"
            
        if lst[0].isalpha()==True:
            b="True"
            break
        else:
            b="False"

        if lst[0].isdigit()==True:
            c="True"
            break
        else:
            c="False"
            
        if lst[0].islower()==True:
            d="True"
            break
        else:
            d="False"
            
        if lst[0].isupper()==True:
            e="True"
            break
        else:
            e="False"
            
        
        lst.pop(0)
        
    print (a)
    
    print (b)
    
    print (c)
    
    print (d)
    
    print (e)
