x = int(input())
s=0
for i in range(2,x):
    if x%i==0:
        s=s+1
if s==0:
    print("prime")
else:
    print("not a prime")