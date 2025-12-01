n=int(input())
l=list(map(int,input().split()))
maximum=max(l)
minimum=min(l)
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
a=d[maximum]
b=d[minimum]
if maximum==minimum:
    print(maximum-minimum,n*(n-1)//2)
else:
    print(maximum-minimum,a*b)
