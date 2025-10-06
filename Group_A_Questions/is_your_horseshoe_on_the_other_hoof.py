l=list(map(int,input().split()))
v=[]
count=0
for i in l:
    if i not in v:
        v.append(i)
    else:
        count+=1
print(count)
