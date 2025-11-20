a=input()
count=1
ans=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count+=1
    else:
        ans=max(ans,count)
        count=1
ans=max(ans,count)
if ans>=7:
    print("YES")
else:
    print("NO")
