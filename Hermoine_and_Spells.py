a, b, c = map(int, input().split())
if a+b > a+c and a+b> b+c:
    print(a+b)
elif a+c > a+b and a+c > b+c:
    print(a+c)
else:
    print(b+c)