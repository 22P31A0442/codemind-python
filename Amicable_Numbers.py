x = int(input())
y = int(input())
s=0
f=0
for i in range(1,x):
    if x%i==0:
        s=s+i
for j in range(1,y):
    if y%j==0:
        f=f+j
if x==f and y==s:
    print("Amicable")
else:
    print("Not Amicable")