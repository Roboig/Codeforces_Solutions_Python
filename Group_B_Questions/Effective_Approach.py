n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
count1=0
count2=0
d1={}
d2={}
for i,j in enumerate(l1):
    d1[j]=i
for i,j in enumerate(l1[::-1]):
    d2[j]=i
for i in l2:
    if i in d1:
        count1+=d1[i]+1
    if i in d2:
        count2+=d2[i]+1
print(count1,count2)
