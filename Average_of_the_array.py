def sls(n,a):
    s = sum(a)/n
    print(f"{s:.2f}")
n = int(input())
a = list(map(int, input().split()))
sls(n,a)