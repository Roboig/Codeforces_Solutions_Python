n=int(input())
l=[]
for _ in range(n):
    a=list(map(int,input().split()))
    l.append(a)
passengers=0
cur_pass=0
for i in l:
    cur_pass-=i[0]
    cur_pass+=i[1]
    passengers=max(passengers,cur_pass)
print(passengers)
