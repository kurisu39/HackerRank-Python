if __name__ == '__main__':
    N = int(input())
    arr = list()
    
    for _ in range (N):
        enter= (input ()).split(' ')
        
        if enter[0]=="insert":
            arr.insert(int(enter[1]),int (enter[2]))

        if enter[0]=="print":
            print(arr)

        if enter[0]=="remove":
            arr.remove(int(enter[1]))
            
        if enter[0]=="append":
            arr.append(int(enter[1]))
            
        if enter[0]=="sort":
            arr.sort

        if enter[0]=="pop":
            arr.pop()
            
        if enter[0]=="reverse":
            arr.reverse()
            