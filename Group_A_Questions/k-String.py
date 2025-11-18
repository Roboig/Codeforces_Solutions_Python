n=int(input())
a=input()
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
ans=""
for i,j in d.items():
    if j%n!=0:
        break
    else:
        ans+=i*(j//n)
if len(a)%n==0 and len(a)//n==len(ans):
    print(ans*n)
elif n==1:
    print(a)
else:
    print(-1)
