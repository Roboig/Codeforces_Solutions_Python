n,m=map(int,input().split())
l=list(map(int,input().split()))
cur=l[0]
count=l[0]-1
for i in l[1:]:
    if i<cur:
        count+=abs(cur-n)+abs(1-i)+1
    else:
        count+=(i-cur)
    cur=i
print(count)
