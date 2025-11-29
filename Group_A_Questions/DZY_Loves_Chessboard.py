n,m=map(int,input().split())
l=[]
for i in range(n):
    a=list(map(str,input()))
    l.append(a)
for i in range(n):
    for j in range(m):
        if ((i%2==0 and j%2==0) or (i%2!=0 and j%2!=0)) and l[i][j]==".":
            l[i][j]="B"
        elif ((i%2!=0 and j%2==0) or (i%2==0 and j%2!=0)) and l[i][j]==".":
            l[i][j]="W"
for i in l:
    print("".join(i))
