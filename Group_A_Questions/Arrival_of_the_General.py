n=int(input())
l=list(map(int,input().split()))
maximum=l[0]
minimum=l[0]
min_index=0
max_index=0
for i in range(n):
    if l[i]>maximum:
        maximum=l[i]
        max_index=i
    if l[i]<=minimum:
        minimum=l[i]
        min_index=i
a=n-1-min_index
b=max_index-0
if min_index>max_index:
    print(a+b)
else:
    print(a+b-1)
