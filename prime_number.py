x = int(input())
f=0
for i in range(2, x):
    if x%i==0:
        f=f+1
if f>=1:
    print("not a prime")
else:
    print("prime")
