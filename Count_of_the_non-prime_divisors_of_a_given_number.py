n = int(input())
s=0
x=0
f=0
for i in range(1,n+1):
    if n%i==0:
        f=f+1
        for j in range(1, i+1):
            if i%j==0:
                s=s+1
        if s==2:
            x=x+1
        s=0
print(f-x)
                