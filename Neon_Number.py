n = int(input())
x = n**2
s=0
while x>0:
    r = x%10
    x = x//10
    s = s+r
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")