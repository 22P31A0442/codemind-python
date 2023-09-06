a = int(input())
b = int(input())
s=0
for i in range(a, b+1):
    q=i
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if s==i:
        print(i, end=' ')
    s=0