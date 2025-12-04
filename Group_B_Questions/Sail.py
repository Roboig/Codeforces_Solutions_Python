t,sx,sy,ex,ey=map(int,input().split())
s=input()
ans=0
for i,j in enumerate(s):
    if sx==ex and sy==ey:
        break
    if sx<ex:
        if j=="E":
            sx+=1
            ans=max(ans,i+1)
    if sx>ex:
        if j=="W":
            sx-=1
            ans=max(ans,i+1)
    if sy<ey:
        if j=="N":
            sy+=1
            ans=max(ans,i+1)
    if sy>ey:
        if j=="S":
            sy-=1
            ans=max(ans,i+1)
if ans<=t and sx==ex and sy==ey:
    print(ans)
else:
    print(-1)
