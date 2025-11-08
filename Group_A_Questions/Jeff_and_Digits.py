n=int(input())
l=list(map(int,input().split()))
count_5=0
count_0=0
for i in l:
    if i==5:
        count_5+=1
    else:
        count_0+=1
if count_5==0 and count_0>=1:
    print(0)
elif count_5>=1 and count_0==0:
    print(-1)
else:
    if count_5>=9:
        print(("5"*9)*(count_5//9)+"0"*count_0)
    else:
        print(0)
