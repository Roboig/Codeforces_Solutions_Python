n=int(input())
d={}
for i in range(n):
    a=input()
    if a not in d:
        d[a]=0
        d[a]+=1
    else:
        d[a]+=1
m=max(d.values())
for i,j in d.items():
    if j==m:
        print(i)
        break
