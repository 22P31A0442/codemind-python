a, b, c = map(int,input().split())
x = a//(b*c)
y = a%(b*c)
if y ==0:
    print(x)
else:
    print(x+1)