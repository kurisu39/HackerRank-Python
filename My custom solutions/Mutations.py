def mutate_string(string, position, character):

    l=list(string)
    l[position]=character
    string = ''.join(l)
    print (string) 
    
    return 

if __name__ == '__main__':
    string=input()
    line=input()
    
    lst=list(line)
    lst.remove(" ")
    position=int(lst[0])
    character=lst[1]
    
    mutate_string(string, position, character)