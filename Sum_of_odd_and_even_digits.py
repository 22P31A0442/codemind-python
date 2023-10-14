n = int(input())
a = list(map(int, input().split()))
s=0
f=0
for i in range(0, n):
    if i%2==0:
        s=s+a[i]
    else:
        f=f+a[i]
if s-f==0:
    print("YES")
else:
    print("NO")