n=int(input())
l=[]
count_1_left=0
count_0_left=0
count_1_right=0
count_0_right=0
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
for i in range(n):
    if l[i][0]==1:
        count_1_left+=1
    else:
        count_0_left+=1
for i in range(n):
    if l[i][1]==1:
        count_1_right+=1
    else:
        count_0_right+=1
a=min(count_1_left,count_0_left)
b=min(count_1_right,count_0_right)
print(a+b)
