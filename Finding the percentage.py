if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    lst=[]
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    
    valor=student_marks[query_name]
    sumbruh=0
    for bruh in valor:
        sumbruh += bruh
        
    pro=sumbruh/len(valor)
    print (format (pro, '.2f'))
    
    
    
