from math import ceil
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
n=l1[0]
m=l1[1]
d={}
temp={}
for i,j in enumerate(l2):
    d[i+1]=j
for i in d:
    temp[i]=ceil(d[i]/m)
a=temp.values()
maximum=max(a)
ans=0
for i,j in temp.items():
    if j==maximum:
        ans=max(ans,i)
print(ans)
