n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
s=0
for i in l[:m]:
    if i<0:
        s+=i
print(-1*s)
