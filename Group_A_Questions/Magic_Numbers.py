a=int(input())
ans=True
while a:
    if a%10==4:
        a=a//10
        if a%10==4:
            a=a//10
            if a%10!=1:
                ans=False
                break
        elif a%10==1:
            ans=True
            a=a//10
        else:
            ans=False
            break
    elif a%10==1:
        ans=True
        a=a//10
    else:
        ans=False
        break
if ans:
    print("YES")
else:
    print("NO")
