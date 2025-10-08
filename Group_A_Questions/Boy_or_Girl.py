a=input()
v=[]
for i in a:
    if i not in v:
        v.append(i)
if len(v)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
