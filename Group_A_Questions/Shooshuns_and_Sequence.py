n,k=map(int,input().split())
l=list(map(int,input().split()))
g=[l[k-1]]*n
ans=True
for i in range(k,n):
    if l[k-1]==l[i]:
        ans=True
    else:
        ans=False
        break
count=0
if ans:
    for i in range(k-2,-1,-1):
        if l[i]!=l[k-1]:
            count=i+1
            break
    print(count)
else:
    print(-1)
