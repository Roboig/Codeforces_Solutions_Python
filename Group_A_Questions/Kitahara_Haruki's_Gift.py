n=int(input())
l=list(map(int,input().split()))
d={100:0,200:0}
for i in l:
    d[i]+=1
if n==1:
    print("NO")
elif d[100]%2!=0:
    print("NO")
else:
    if d[200]%2!=0 and d[100]==0:
        print("NO")
    else:
        print("YES")
