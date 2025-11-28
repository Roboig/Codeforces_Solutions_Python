n,m=map(int,input().split())
l=list(map(int,input().split()))
ans1,ans2=0,0
a=l[:]
for i in range(n):
    m=min(a)
    if m==1:
        index=a.index(m)
        a.pop(index)
        ans1+=1
    else:
        index=a.index(m)
        a[index]=m-1
        ans1+=m
for i in range(n):
    m=max(l)
    index=l.index(m)
    l[index]=m-1
    ans2+=m
print(ans2,ans1)
