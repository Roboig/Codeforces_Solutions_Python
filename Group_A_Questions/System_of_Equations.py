n,m=map(int,input().split())
minimum=min(n,m)
count=0
for a in range(minimum+1):
    for b in range(minimum+1):
        if (a**2+b)==n and (a+b**2)==m:
            count+=1
print(count)
