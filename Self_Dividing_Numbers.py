a = int(input())
b = int(input())
s=0
f=0
x=0
for i in range(a, b+1):
    q=i
    if i<10:
        print(i, end=' ')
    else:
        while q!=0:
            r = q%10
            s=s+1
            q=q//10
            if r==0:
                break
            elif i%r==0:
                f=f+1
        if s==f:
            print(i, end=' ')
        f=0
        s=0
        x=0
            