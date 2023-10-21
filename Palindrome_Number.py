n = int(input())
for i in range(1, n+1):
    a = int(input())
    q=a
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if a==s:
        print("True")
    else:
        print("False")