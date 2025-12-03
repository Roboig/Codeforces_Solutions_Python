from collections import Counter
s=input()
d=Counter(s)
count=0
for i in d.values():
    if i%2!=0:
        count+=1
if count==0 or count%2==1:
    print("First")
else:
    print("Second")
