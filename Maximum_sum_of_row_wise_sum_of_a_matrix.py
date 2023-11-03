r, c = map(int, input().split())
matrix = []
s=0
for i in range(r):
    a = list(map(int, input().split()))
    x = sum(a)
    if x>s:
        s=x
print(s)