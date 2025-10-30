n=int(input())
l=list(map(int,input().split()))
s=sum(l)
dima=1
l1=[]
while dima<=s+5:
    l1.append(dima)
    dima+=n+1
count=0
for i in range(1,6):
    if s+i not in l1:
        count+=1
print(count)
