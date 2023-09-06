n = int(input())
s=0
f=0
x=0
for i in range(1, n+1):
    if n%i==0:
        s=s+1
        for j in range(1, i+1):
            if i%j==0:
                f=f+1
        if f==2:
            x=x+1
        f=0
print(s-x)
    