n = int(input())
a = list(map(int, input().split()))
s=0
for i in a:
    if i%2!=0:
        print("False")
        break
    else:
        s=s+1
if s==n:
    print("True")