n = int(input())
f=1
s=0
q=n
while q!=0:
    r=q%10
    for i in range(1, r+1):
        f=f*i
    s=s+f
    q=q//10
    f=1
if s==n:
    print(f"The number {n} is a strong number")
else:
    print(f"The number {n} is not a strong number")