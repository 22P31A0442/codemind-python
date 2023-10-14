n = int(input())
a = list(map(int, input().split()))
s=0
for i in a:
    if i==1 or i==0:
        s=s+1
    else:
        print("False")
        break
if s==n:
    print("True")