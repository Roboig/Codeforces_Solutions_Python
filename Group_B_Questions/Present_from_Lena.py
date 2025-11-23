n=int(input())
j=1
while j<=n+1:
    ans=""
    for k in range(j):
        ans+=f"{k} "
    if len(ans)>=2:
        suffix=ans[:-2]
    else:
        suffix=""
    ans="  "*(n-j+1)+ans+suffix[::-1].strip()
    print(ans.rstrip())
    j+=1
j=n
while j>=0:
    ans=""
    for k in range(j):
        ans+=f"{k} "
    if len(ans)>=2:
        suffix=ans[:-2]
    else:
        suffix=""
    ans="  "*(n-j+1)+ans+suffix[::-1].strip()
    print(ans.rstrip())
    j-=1
