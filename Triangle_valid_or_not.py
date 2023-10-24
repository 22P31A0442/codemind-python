def sls(a, b,c):
    if a+b>c and a+c>b and b+c>a:
        return 'Valid triangle'
    else:
        return 'Invalid triangle'
a, b, c = map(int, input().split())
print(sls(a, b, c))