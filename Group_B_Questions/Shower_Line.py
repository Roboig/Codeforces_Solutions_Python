from itertools import permutations
g=[]
for i in range(5):
    a=list(map(int,input().split()))
    g.append(a)
a="12345"
ans=0
p=permutations(a)
for i in p:
    t0,t1,t2,t3,t4=int(i[0])-1,int(i[1])-1,int(i[2])-1,int(i[3])-1,int(i[4])-1
    s=g[t0][t1]+g[t1][t0]+2*(g[t2][t3]+g[t3][t2])+g[t1][t2]+g[t2][t1]+2*(g[t3][t4]+g[t4][t3])
    ans=max(ans,s)
print(ans)
