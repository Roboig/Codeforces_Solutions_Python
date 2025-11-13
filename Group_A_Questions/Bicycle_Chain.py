n=int(input())
l=list(map(int,input().split()))
m=int(input())
g=list(map(int,input().split()))
k=[]
ans=0
for i in range(m):
    for j in range(n):
        if g[i]%l[j]==0:
            a=g[i]/l[j]
            k.append(a)
            ans=max(ans,a)
count=0
for i in k:
    if i==ans:
        count+=1
print(count)
