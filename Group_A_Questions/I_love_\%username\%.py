n=int(input())
l=list(map(int,input().split()))
maximum=l[0]
minimum=l[0]
total=0
for i in l[1:]:
    if i>maximum:
        maximum=i
        total+=1
    if i<minimum:
        minimum=i
        total+=1
print(total)
