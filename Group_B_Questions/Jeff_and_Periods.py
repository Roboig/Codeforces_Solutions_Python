n=int(input())
l=list(map(int,input().split()))
d={}
for i,j in enumerate(l):
    if j not in d:
        d[j]=[i]
    else:
        d[j].append(i)
ans={}
for i,j in d.items():
    if len(j)==1:
        ans[i]=0
    elif len(j)==2:
        ans[i]=j[1]-j[0]
    else:
        d1=j[1]-j[0]
        res=False
        for k in range(len(j)-1):
            diff=j[k+1]-j[k]
            if diff==d1:
                res=True
            else:
                res=False
                break
        if res:
            ans[i]=d1
print(len(ans))
for i,j in sorted(ans.items()):
    print(i,j)

