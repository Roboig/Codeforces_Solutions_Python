s=input()
j=0
l=["h","e","l","l","o"]
for i in s:
    if i==l[j]:
        j+=1
    if j==5:
        break
if j==5:
    print("YES")
else:
    print("NO")
