x = int(input())
s=0
for i in range(1,x+1):
    if i*(i+1)==x:
        s=s+1
if s==1:
    print("YES")
else:
    print("NO")