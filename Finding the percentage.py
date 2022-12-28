if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    lst=[]
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        lst.append(student_marks)
    query_name = input()
    
    print (lst)
    