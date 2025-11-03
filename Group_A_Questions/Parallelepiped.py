g=list(map(int,input().split()))
f1=g[0]
f2=g[1]
f3=g[2]
b=((f1*f3)/f2)**(1/2)
l=f1/b
h=f3/b
print(int(4*(l+b+h)))
