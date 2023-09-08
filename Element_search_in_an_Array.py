n = int(input())
a = list(map(int, input().split()))
x = int(input())
s=0
for i in range(0,n):
    if a[i]==x:
        s=s+1
if s>=1:
    print("True")
else:
    print("False")