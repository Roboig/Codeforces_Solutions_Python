s1=input()
s2=input()
for i in s2:
    if i in s1:
        s1=s1.replace(i,"",1)
        s2=s2.replace(i,"",1)
    elif i==" ":
        s2=s2.replace(i,"",1)
        pass
    else:
        break
if s2=="":
    print("YES")
else:
    print("NO")
