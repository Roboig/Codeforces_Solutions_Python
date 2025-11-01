n=int(input())
g=[]
for i in range(n):
    l=tuple(map(int,input().split()))
    g.append(l)
count=0
for i in g:
    rn=0
    ln=0
    ln1=0
    un=0
    for j in g:
        if j[0]>i[0] and j[1]==i[1]:
            rn+=1
        if j[0]<i[0] and j[1]==i[1]:
            ln+=1
        if j[1]>i[1] and j[0]==i[0]:
            ln1+=1
        if j[1]<i[1] and j[0]==i[0]:
            un+=1
    if rn>=1 and ln>=1 and ln1>=1 and un>=1:
        count+=1
print(count)
