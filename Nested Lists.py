if __name__ == '__main__':
    lst = []
    lst2= []
    lst3= []
    n = int(input())
    max=0

    for i in range(0, n):
        ele = [input(), float(input())]
        if ele[1]>max:
            max=ele[1]     
        lst.append(ele)
    min=max

    for min_lst in lst:
        if min>min_lst[1]:
            min=min_lst[1]   

    for second_lst in lst:
        if second_lst[1]==min:
            second_lst.remove(second_lst[1])
            second_lst.remove(second_lst[0])
        lst2.append(second_lst)
    
    for moremin_lst in lst2:
        try:
            if max>moremin_lst[1]:
                max=moremin_lst[1]  
        except: pass

    lol=""
    lst4=[]
    for alfin_lst in lst2:
        try:
            if max==alfin_lst[1]:
                lol=alfin_lst[0]
                lst4.append(lol)
        except: pass

    
    for alfin in sorted (lst4):
        print (alfin)