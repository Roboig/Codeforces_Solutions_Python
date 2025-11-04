n=int(input())
l=list(map(int,input().split()))
d={}
for i in range(n):
    if i+1>=n:
        a=(i+1)%n
        diff=abs(l[i]-l[a])
        d[(i+1,a+1)]=diff
    else:
        diff=abs(l[i]-l[i+1])
        d[(i+1,i+2)]=diff
m=min(d.values())
for i,j in d.items():
    if j==m:
        a,b=i
        print(a,b)
        break
