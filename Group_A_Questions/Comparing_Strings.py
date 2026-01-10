a=input()
b=input()
count=0
if len(a)==len(b):
    ans=True
    for i in range(len(a)):
        if a[i]!=b[i]:
            if b[i] not in a:
                ans=False
                break
            count+=1
    if count==2 and ans==True:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
