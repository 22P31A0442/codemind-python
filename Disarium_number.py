n = int(input())
s=0
x = len(str(n))
q=n
while q!=0:
    r=q%10
    s=s+r**x
    x=x-1
    q=q//10
if n==s:
    print("True")
else:
    print("False")