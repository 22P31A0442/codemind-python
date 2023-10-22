def sls(a):
    if a>20:
        return 'HOT'
    elif a<=20:
        return 'COLD'
a = int(input())
print(sls(a))