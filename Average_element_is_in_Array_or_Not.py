def sls(n, a, s):
    f=0
    for i in range(0, n):
        if a[i]==s:
            f=f+1
    if f>=1:
        return True
    else:
        return False


n = int(input())
a = list(map(int, input().split()))
s = sum(a)//n
print(sls(n,a,s))
