n=int(input())
count=0
for i in range(10000000-n+1,10000001):
    count+=1
    print(i,end=" ")
    if count==n:
        break
    
    
