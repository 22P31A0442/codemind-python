x = int(input())
a = 0
b = 1
print(f"{a} {b}", end=' ')
for i in range(1, x-1):
    c = a+b
    print(c, end=' ')
    a=b
    b=c