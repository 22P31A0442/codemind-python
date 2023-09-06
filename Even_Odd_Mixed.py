n = int(input())
s=0
x=0
y=0
while n!=0:
    r=n%10
    s=s+1
    if r%2==0:
        x=x+1
    else:
        y=y+1
    n=n//10
if x==s:
    print("Even")
elif y==s:
    print("Odd")
else:
    print("Mixed")