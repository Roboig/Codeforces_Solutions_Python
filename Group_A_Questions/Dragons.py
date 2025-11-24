s,n=map(int,input().split())
ans=False
g=[]
for i in range(n):
    l=list(map(int,input().split()))
    g.append(l)
g.sort()
for i in g:
    if s>i[0]:
        s+=i[1]
        ans=True
    else:
        ans=False
        break
if ans:
    print("YES")
else:
    print("NO")
