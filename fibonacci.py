a = int(input())
x = 0
y = 1
print(x,y,end=' ')
for i in range(1, a-1):
    z = x+y
    print(z,end=' ')
    x=y
    y=z