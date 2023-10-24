def sls(a, b, c, d):
    if a>=10 and b>=10 and c>=10 and d>=10:
        return 'YES'
    else:
        return 'NO'
a, b, c, d = map(int, input().split())
print(sls(a, b, c, d))