n = int(input())
a = list(map(int, input().split()))
x, y = map(int,input().split())
s=0
for i in a:
    if i<x or i>y:
        print(i, end=' ')
        s=s+1
if s==0:
    print("-1")