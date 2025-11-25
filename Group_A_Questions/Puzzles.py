n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
ans=float("inf")
for i in range(m):
    a=l[i:i+n]
    if len(a)==n:
        ans=min(ans,a[-1]-a[0])
print(ans)
