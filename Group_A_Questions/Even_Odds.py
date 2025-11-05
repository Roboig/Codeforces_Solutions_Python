n,k=map(int,input().split())
odd=(n+1)//2
if k<=odd:
    ans=k*2-1
else:
    even=k-odd
    ans=even*2
print(ans)
