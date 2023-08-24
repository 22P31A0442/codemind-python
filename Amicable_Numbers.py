a = int(input())
b = int(input())
s = 0
f = 0
for i in range(1, a):
    if a%i==0:
        s = s+i
for j in range(1, b):
    if b%j==0:
        f=f+j
if s==b and f==a:
    print("Amicable")
else:
    print("Not Amicable")