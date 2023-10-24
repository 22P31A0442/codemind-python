def sls(n):
    if n%2!=0:
        return 'weird'
    elif n%2==0 and n>=6 and n<=20:
        return 'weird'
    else:
        return 'not weird'
n = int(input())
print(sls(n))