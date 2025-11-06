n=int(input())
l=list(map(int,input().split()))
m=min(l)
a=l.count(m)
if a==1:
    print(l.index(m)+1)
else:
    print("Still Rozdil")
