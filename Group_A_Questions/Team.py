n=int(input())
ans=0
for i in range(n):
    l=list(map(int,input().split()))
    count=0
    for i in l:
        if i==1:
            count+=1
    if count>=2:
        ans+=1
print(ans)
