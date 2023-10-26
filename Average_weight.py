def sls(a, b ,c):
    x = 3*a-b-c
    return x
a, b, c = map(int, input().split())
print(sls(a, b,c))