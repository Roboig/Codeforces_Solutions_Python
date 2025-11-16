k=int(input())
l=list(map(int,input().split()))
l.sort()
s=0
flag=False
count=0
for i in l[::-1]:
    if s>=k:
        flag=True
        break
    count+=1
    s+=i
if s>=k:
    flag=True
if flag:
    print(count)
else:
    print(-1)
