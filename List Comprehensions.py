#############Flex $hit$$$$$$$$$$$$$$$$$$$$
x= int(input("First: "))
y= int(input("Second: "))
z= int(input("Third: "))

n= int(input("Sum: "))

i=0
j=0
k=0

iterable=[i,j,k]
grand=[]

for shit in range (x+y+z):
   if iterable[0]<x:
      iterable[0]+=1
      
      if iterable[0]>n:
         iterable[0]=0
         
         if iterable[1]<y:
            iterable[1]+=1
            
         if iterable[2]<z:
            iterable[2]+=1

   else: break
   grand.append(iterable)
   
print(grand)
   