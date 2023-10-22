def sls(a, b):
    if a>b:
        return 'Loss'
    elif a<b:
        return 'Profit'
    else:
        return 'No Profit and No Loss'
a = int(input())
b = int(input())
print(sls(a,b))