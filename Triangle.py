def sls(a, b,c):
    if a==b==c:
        return 'Equilateral triangle'
    elif a==b or a==c or b==c:
        return 'Isosceles triangle'
    else:
        return 'Scalene triangle'
a, b, c = map(int,input().split())
print(sls(a,b,c))