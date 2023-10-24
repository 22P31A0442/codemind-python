def sls(n):
    s=0
    for i in range(1, n+1):
        if n%i==0:
            s=s+1
    if s==2:
        return 'Prime'
    else:
        return 'Not Prime'
n = int(input())
print(sls(n))