n = int(input())
a = 0
b = 1
s=0
while True:
    c=a+b
    if c==n:
        print("True")
        s=s+1
        break
    if c>n:
        break
    a = b
    b = c
if s==0:
    print("False")