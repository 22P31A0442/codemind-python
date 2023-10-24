def sls(n):
    q=n
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if s==n:
        return 'Palindrome'
    else:
        return 'Not Palindrome'
n = int(input())
print(sls(n))