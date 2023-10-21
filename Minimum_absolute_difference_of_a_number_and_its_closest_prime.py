n = int(input())
s=0
for i in range(1, n+1):
    if n%i==0:
        s=s+1
if s==2:
    print("0")
else:
    f=0
    q=n
    while True:
        q=q+1
        for j in range(1,q+1):
            if q%j==0:
                f=f+1
        if f==2:
            break
        f=0
    g=0
    p=n
    while True:
        p=p-1
        for k in range(1,q+1):
            if p%k==0:
                g=g+1
        if g==2:
            break
        g=0
    if q-n<n-p:
        print(abs(n-q))
    else:
        print(abs(n-p))
        