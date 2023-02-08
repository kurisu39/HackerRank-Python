def count_substring(string, sub_string):
    count=0
    len_sub_string=len(sub_string)
    list1 = []
    list1[:0] = string
    list2 = []
    list2[:0] = sub_string
    
    for i in range(0, len(string)):


        if list1[0:len_sub_string]==list2:
            count+=1
       
        list1.pop(0)
    return str(count)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
    #holaacreholaholaacreholaholx