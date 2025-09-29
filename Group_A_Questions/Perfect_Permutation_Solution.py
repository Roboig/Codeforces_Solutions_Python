n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
if n%2==1:
    print(-1)
else:
    i=0
    while i<n-1:
        temp=l[i]
        l[i]=l[i+1]
        l[i+1]=temp
        i+=2
    print(*l)
