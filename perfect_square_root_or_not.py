x = int(input())
s=0
for i in range(1, x//2+1):
    if i*i==x:
        s=s+1
if s==1:
    print("True")
else:
    print("False")