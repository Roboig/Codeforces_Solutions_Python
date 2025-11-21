a=input()
ans=""
for i in a:
    if i.upper() in ["A","E","I","O","U","Y"]:
        pass
    else:
        ans+="."+i.lower()
print(ans)
