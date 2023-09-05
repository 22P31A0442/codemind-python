n = int(input())
s=0
for i in range(1, n+1):
    x = int(input())
    for j in range(1,x+1):
        if j*j==x:
            s=s+1
    if s==1:
        print("True")
    else:
        print("False")
    s=0
    