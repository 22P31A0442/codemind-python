n = int(input())
x = len(str(n))
s=0
y=0
q=n
while q!=0:
    r = q%10
    s=s+1
    m = r**(x+1-s)
    y=y+m
    q=q//10
if n==y:
    print("True")
else:
    print("False")