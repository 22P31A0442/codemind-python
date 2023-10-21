n = int(input())
s=0
a = list(map(int, input().split()))
for i in a:
    s=s+i
if s%2==0:
    print("1")
else:
    print("0")