s=input()
t=input()
if s.lower()==t[::-1].lower():
    print("YES")
else:
    print("NO")
