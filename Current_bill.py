def sls(n):
    if n<=199:
        u = 1.20
        s=100
    elif n>=200 and n<400:
        u=1.50
        s=100
    elif n>=400 and n<600:
        u=1.80
        s=n*u*0.15
    else:
        u=2
        s=n*u*0.15
    return n*u+s
n = int(input())
print(f"{(sls(n)):.2f}")