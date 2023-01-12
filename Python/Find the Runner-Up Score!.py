if __name__ == '__main__':
    
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]

    great_number=max(arr)
    
    arr = [i for i in arr if i < great_number]
    
    largest_number=arr[0]
    
    for number in arr:
        if number > largest_number:
            largest_number = number
    print(largest_number)
    
    
