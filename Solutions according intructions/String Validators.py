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
        
        if lst[0].isalnum()==True:
            a="True"
            
        else:
            if a=="True":
                a="True"
            else:
                a="False"
            
        if lst[0].isalpha()==True:
            b="True"
         
        else:
            if b=="True":
                b="True"
            else:
                b="False"
            

        if lst[0].isdigit()==True:
            c="True"
            
        else:
            if c=="True":
                c="True"
            else:
                c="False"
            
        if lst[0].islower()==True:
            d="True"
          
        else:
            if d=="True":
                d="True"
            else:
                d="False"
            
        if lst[0].isupper()==True:
            e="True"
           
        else:
            if e=="True":
                e="True"
            else:
                e="False"
            
        
        lst.pop(0)
        
    print (a)
    
    print (b)
    
    print (c)
    
    print (d)
    
    print (e)
