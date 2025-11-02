n=int(input())
l=list(map(int,input().split()))
i=0
while i<len(l):
    n=n-l[i]
    if n<=0:
        print(i+1)
        break
    i+=1
    i=i%len(l)
